from opcua import Server
import random
import time
from datetime import datetime

server = Server()
server.set_endpoint("opc.tcp://localhost:4840")

uri = "http://example.opcua.assignment"
idx = server.register_namespace(uri)

objects = server.get_objects_node()

my_object = objects.add_object(idx, "MySimulation")

variables = []
for i in range(1, 11):
    var = my_object.add_variable(idx, f"Tag{i}", 0.0)
    var.set_writable()
    variables.append(var)

server.start()
print("OPC UA Server started at opc.tcp://localhost:4840")

try:
    while True:
        for var in variables:
            value = random.uniform(10, 100)
            var.set_value(value)
        print("Updated values at", datetime.now())
        time.sleep(5)

except KeyboardInterrupt:
    print("Shutting down server...")

finally:
    server.stop()
