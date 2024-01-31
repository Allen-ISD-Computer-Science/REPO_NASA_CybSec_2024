import os
import socket
import sys

# Set Port Number, File Name, and Host IP
port = int(input("Port: "))
host = str(input("IP: "))
fileName = str(input("Name of the file: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Send Size
file = open(fileName, "rb")
file_size = os.path.getsize(fileName)

# Send Extension
client.send(fileName.encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()
sys.exit(0)

# Sockets: https://docs.python.org/3/library/socket.html
# Subprocesses: https://docs.python.org/3/library/subprocess.html
# Should hash file, filepath, 
# send and get hash function 