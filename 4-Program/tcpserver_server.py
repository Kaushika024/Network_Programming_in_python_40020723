import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
s.listen(1)
print("Waiting for any incoming connections ... ")
conn,addr = s .accept()
print(addr,"Has connected to the server")

filename = input(str("Please enter the filename of the file: "))
#open in readby its mode
file = open(filename,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")
