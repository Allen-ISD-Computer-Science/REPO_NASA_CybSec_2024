import socket
import sys
# Progress bar (pip install tqdm) later

# Set Port and IP
#port = int(input("Port: "))
#host = str(input("IP: "))
port = 3000
host = "localhost"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, addr = server.accept()

# Recieve specified amount of bytes
nameRecieved = False
sizeRecieved = False
file_name = ""
file_size = ""

while not nameRecieved:
    file_name += client.recv(1).decode("utf-8", "ignore")
    if file_name == "example.txt":
        nameRecieved = True
print(f"{file_name}\n")

file_size = client.recv(2048)
print(f"{file_size}\n")

file = open(file_name, "wb")
file_bytes = b""

done = False

while not done:
    data = client.recv(2048)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes += data

file.write(file_bytes)

file.close()
client.close()
server.close()

sys.exit(0)