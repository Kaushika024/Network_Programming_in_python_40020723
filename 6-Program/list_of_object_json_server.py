import socket
import sys
import json

s = socket.socket()
print('Connection Established')
print('Fetching data...')

port = 1500
address = '127.0.0.1'
s.bind((address,port))

jsonResult = {"NAME":"KAUSHI","PSNO":"40020723","BU":"EMBEDDED V&V","TRACK":"PYTHON ATF"}
jsonResult = json.dumps(jsonResult).encode('utf-8')

s.listen(1)

while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected to ",addr,name)
    data1 = jsonResult
    c.send(data1)
    
    c.close()
