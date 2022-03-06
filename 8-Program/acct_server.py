import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 20202
host = socket.gethostbyname(socket.gethostname())
s.bind((host,port))

s.listen()

while True:
    c,addr = s.accept()

    print('json Decoded ')
    jsonstr1= c.recv(1024).decode('utf-8')
    print(jsonstr1)

    jsonstr2= c.recv(1024).decode('utf-8')
    print(jsonstr2)

    jsonstr3= c.recv(1024).decode('utf-8')
    print(jsonstr3)

    jsonstr4= c.recv(1024).decode('utf-8')
    print(jsonstr4)

    jsonstr5= c.recv(1024).decode('utf-8')
    print(jsonstr5)

    jsonstr6= c.recv(1024).decode('utf-8')
    print(jsonstr6)

    jsonstr7= c.recv(1024).decode('utf-8')
    print(jsonstr7)

    jsonstr8= c.recv(1024).decode('utf-8')
    print(jsonstr8)

    c.close()
