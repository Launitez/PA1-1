

#Create the client socket for connection
import socket

HOST= "127.0.0.1"
PORT= 3185

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected to the server successfully!")

#Sending data to server
s.sendall(b"Hello, server!")
data = s.recv(1024)

print(f"Received {data.decode()}")