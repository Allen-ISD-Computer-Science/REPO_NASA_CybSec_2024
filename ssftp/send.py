# Instructions to send files over UDP
# sudo ufw allow #port/udp
# cat file.jpg | nc -u 192.168.x.x #port (on the source machine)


import os
import socket
import sys

# Set Port Number, File Name, and Host IP
#port = int(input("Port: "))
#host = str(input("IP: "))
port = 3000
host = "localhost"
#fileName = str(input("Name of the file: "))
fileName = "example.txt"

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
