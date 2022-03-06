import socket
import sys

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',12345)

client.connect(server_address)
quit = 'cquit'
msg = input()
print("SENDING",msg)
client.sendall(msg.encode())
print("ORIGINAL: ",msg)

#receive the data
data = client.recv(1000).decode()
if data == quit:
    print("Client will perform active close")
    client.close()
else:
    i=0
    while True:
        while(i<=5):
            print("ECHO: ",data)
            i+=1
        client.close()

