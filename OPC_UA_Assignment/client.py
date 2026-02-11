from opcua import Client
import pandas as pd
import time
import os
from datetime import datetime

url = "opc.tcp://localhost:4840"
client = Client(url)
client.connect()

print("Connected to Server")

base_node = client.get_objects_node().get_child(["2:MySimulation"])

nodes = []
for i in range(1, 11):
    node = base_node.get_child([f"2:Tag{i}"])
    nodes.append(node)

if not os.path.exists("logs"):
    os.makedirs("logs")

current_hour = None
file_name = None

try:
    while True:
        now = datetime.utcnow()
        hour_str = now.strftime("%Y-%m-%d_%H")

        if hour_str != current_hour:
            current_hour = hour_str
            file_name = f"logs/OPC_Log_{hour_str}.csv"
            df = pd.DataFrame(columns=[
                "Timestamp_UTC", "EpochTime",
                "Tag1","Tag2","Tag3","Tag4","Tag5",
                "Tag6","Tag7","Tag8","Tag9","Tag10"
            ])
            df.to_csv(file_name, index=False)
            print("Created new file:", file_name)

        values = [node.get_value() for node in nodes]

        row = [
            now.strftime("%Y-%m-%d %H:%M:%S"),
            int(now.timestamp())
        ] + values

        df = pd.DataFrame([row])
        df.to_csv(file_name, mode='a', header=False, index=False)

        print("Logged:", row)

        time.sleep(60)

except KeyboardInterrupt:
    print("Stopping client")

finally:
    client.disconnect()
