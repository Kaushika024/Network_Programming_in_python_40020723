from re import s
import socket 
import sys

c=socket.socket(socket.AF_INET,socket.SOCK_STEARM)

port = 1500
address = '127.0.0.1'
c.connect((address,port))

name = input("Enter your name: ")
c.send(bytes(name,'utf-8'))

#receive the data 
data2 = c.recv(1024).decode('utf-8')
#print  the received data
print(data2)

#close the client
c.close()
