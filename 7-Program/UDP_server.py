import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())

if len(sys.argv)==2:
    port = int(sys.argv[1])

s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Received Request from', addr)
    print('hostname takes from the server details')
    print('port as command line argument')
    c.send(b'Thanks for connecting')
    c.close()
