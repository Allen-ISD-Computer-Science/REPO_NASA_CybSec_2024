# Instructions to set up UDP file receiving
# sudo ufw allow #port/udp
# nc -u -l -p #port > newfile.jpg (on the destination machine)


import socket
import sys
# Progress bar (pip install tqdm) later

# Set Port and IP
port = int(input("Port: "))
host = str(input("IP: "))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

client, addr = server.accept()

# Recieve specified amount of bytes
file_name = client.recv(2048).decode()
print(file_name)
file_size = client.recv(2048)
print(file_size)

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
