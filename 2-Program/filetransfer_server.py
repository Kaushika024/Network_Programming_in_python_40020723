import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 5454
ADDR = (IP, PORT)
FORMAT = "UTF-8"
SIZE = 1024

def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)
    print("[LISTENING] Server is Listening.")

    while True:
        conn, addr = server.accept()
        print(f"[NEW COONNECTION] {addr} connected.")

        filename = conn.recv(SIZE).decode(FORMAT)
        print("[RECEIVED] Filename Received.")
        file = open("server_data/"+filename, "w")
        conn.send("Filename received.".encode(FORMAT))

        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECEIVED] File data received")
        file.write(data)
        conn.send("File data received.".encode(FORMAT))

        file.close()
        conn.close()
        print(f"[DISCONNECTED] {addr} Disconnected.")
        
if __name__=="__main__":
     main()
