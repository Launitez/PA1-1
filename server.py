#Ilaun Baldwin-server implementation

#creating server socket 
import socket
HOST = "127.0.0.1"
PORT = 3185

try:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #binding socket to port and listening for connections from the client
        s.bind((HOST, PORT))
        print(f"Binding successful on {HOST}:{PORT}")
        #Listening for connections
        s.listen(1);
        print(f"Listening on {HOST}:{PORT}...")
        #accepting connections
        conn, addr = s.accept()
        print(f"Connection established with {addr}")
 
except socket.error as e:
    #checking for any errors
    print(f"Socket error: {e}")

#Exchanging data between client and server
with conn:
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
