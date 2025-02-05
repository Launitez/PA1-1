#Create the client socket for connection
import socket

HOST= "127.0.0.1"
PORT= 3185

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
print("Connected to the server successfully!")

#Sending data to server
try:
    s.sendall(b"Hello, server!")
    data = s.recv(1024)
    print(f"Received {data}")
    
finally:
    #close the socket 
    s.close()