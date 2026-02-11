OPC UA Client Development and Data Logging

Project Overview:
This project implements a local OPC UA server and client using Python.
The client reads 10 dummy tags every minute and logs the data into hourly CSV files.

Requirements:
- Python 3.x
- pip
- Libraries:
    pip install opcua pandas

How to Run:

1. Open terminal and navigate to project folder:
   cd OPC_UA_Assignment

2. Start OPC UA Server:
   python server.py

3. Open a new terminal and run client:
   python client.py

4. Logs will be generated in the logs folder.

Output:
- CSV files named as:
  OPC_Log_YYYY-MM-DD_HH.csv
- Each file contains:
  Timestamp (UTC)
  Epoch Time
  Tag1 to Tag10 values

Automation:
- Client runs continuously.
- New CSV file created automatically on hour change.
