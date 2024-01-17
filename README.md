# 5G Smart Production Networking Application

## Overview
This project involves the design and implementation of a networking application that connects a Festo PLC from the AAU 5G Smart Production Lab to a Python server. The primary goal is to establish a TCP connection between the Festo PLC and the server, allowing for communication and control over processing times based on pallet and station IDs.

## Files

### 1. PLC_PRG

- **Description:** This file contains the CODESYS project file (`PLC_PRG`) for the Festo PLC.
- **Usage:** Load this file into the CODESYS development environment to program the PLC.

### 2. CSVAndServer.py

- **Description:** This Python script (`CSVAndServer.py`) acts as the server for the networking application. It handles the TCP connection with the Festo PLC client, parses incoming XML strings, and controls processing times based on the extracted pallet and station IDs.
- **Usage:** Run this script using a Python interpreter (e.g., `python CSVAndServer.py`). Make sure to have the necessary dependencies installed.

### 3. procssing_times_table.csv

- **Description:** This CSV file (`procssing_times_table.csv`) serves as a data table holding processing times for different pallets.
- **Usage:** The server script (`CSVAndServer.py`) references this file to determine processing times based on the received pallet ID.


## Usage

1. **Start the Server:**
   - Run the server script (`CSVAndServer.py`).

2. **Program the PLC:**
   - Load the CODESYS project (`PLC_PRG`) into the Festo PLC using the CODESYS development environment.

3. **Networking:**
   - The server will establish a TCP connection with the PLC.
   - The server will parse incoming XML strings from the PLC client, extracting pallet and station IDs.
   - Based on the IDs, the server will control how long the PLC has to wait, referencing the processing times table.

## Dependencies

- Python 3
- Additional Python packages (install using `pip install -r requirements.txt`):
- CodeSys

## License

This project is licensed under the [MIT License](LICENSE).
