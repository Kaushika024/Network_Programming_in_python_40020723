import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
if len(sys.argv)==2:
    port = int(sys.argv[1])

s.connect((host,port))

print('hostname takes from the server details')
print('port as command line argument')
print(s.recv(1024))

s.close()

