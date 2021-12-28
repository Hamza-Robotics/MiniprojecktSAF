import socket
import xml.sax
import xml.etree.ElementTree as ET
import os

import csv

S=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind(("172.20.66.44",1234))
print(socket.gethostbyname(socket.gethostname()))
S.listen(0)

class FestoHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""


   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag


   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "ID":
         self.ID = content
      elif self.CurrentData == "stationnumber":
         self.stationnumber = content
      elif self.CurrentData == "Error":
         self.Error = content

      self.CurrentData = ""


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def getCarrierNumber(_ID):
    with open('C:\\Users\\SebBl\\Documents\\WrittenPrograms\\CVS\\RFID_Tags.csv') as RFID_TAGS:
        RFID_Reader = csv.reader(RFID_TAGS, delimiter=';')
        row_nr = 0
        for CSV in RFID_Reader:
            if (CSV[1] == _ID):
                return row_nr
            row_nr += 1
        return 1


Handler = FestoHandler()
 
# create an XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.setContentHandler( Handler )


# override the default ContextHandler
Handler = FestoHandler()
clientsocket, address=S.accept();

while True:
    data = clientsocket.recv(1024)
    data=str(data)
    
    XML_string = data[data.find("<pallet>"):data.find("</pallet>")+len("</pallet>")]

    xml.sax.parseString(XML_string, Handler)

    print("Pallet ID: ",Handler.ID)
    if Handler.ID is '0':
        Handler.ID = '1'
    #Handler.ID   denne værdi giver id-til pallet
    #Handler.stationnumber denne giver id til stations number.
    #seconds er tiden man finder fra csv fil.
    if data:
            #seconds er tiden man finder fra csv fil.
            #find seconds
        with open('C:\\Users\\SebBl\\Documents\\WrittenPrograms\\CVS\\procssing_times_table.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            rows = list(csv_reader)
            carrierNumber=getCarrierNumber(Handler.ID)
            seconds = int(rows[carrierNumber][int(Handler.stationnumber)])
            #if Handler.Error is '0':
            print("Carrier Number:", carrierNumber, ", Stations Number:", Handler.stationnumber, ", Waiting for", seconds, "milliseconds", ", Retry?[1/0]: ", Handler.Error)
            seconds = seconds.to_bytes(4,'big')

        clientsocket.send(seconds)


clientsocket.close()