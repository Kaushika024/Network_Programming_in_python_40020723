import socket
import sys

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',12345)
server.bind(server_address)
server.listen(1)
quit = 'squit'

connection,client_address = server.accept()
print("Connection Established with: ",client_address)
data=connection.recv(1000).decode()

if data == quit:
    print("Server will perform active close")
    connection.close()
    server.close()
else:
    while True:
        print("RECEIVED:",data)
        connection.sendall(data.encode())
        connection.close()
        server.close()
