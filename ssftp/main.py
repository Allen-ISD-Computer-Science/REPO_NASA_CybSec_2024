import sys
import argparse
import socket

parser = argparse.ArgumentParser()

parser.add_argument('-s', '--send')
parser.add_argument('-e')
parser.add_argument('filename')

args = parser.parse_args()


def openPort():
    HOST = None
    PORT = 69420 #Set ports that the machine are listening and reciving on
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.blind(sa)
            s.lsiten(1)
        except OSError as msg:
            s.close()
            s = None
            continue
        

# Sockets: https://docs.python.org/3/library/socket.html
# Subprocesses: https://docs.python.org/3/library/subprocess.html
# Should hash file, filepath, 
# send and get hash function 