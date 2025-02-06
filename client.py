#Create the client socket for connection
import socket

HOST= "127.0.0.1"
PORT= 3185 

def sendCommand(s, command, data=None):
    # Sending command to server
    s.sendall(command.encode())
    if data:
        s.sendall(data.encode())
    response = s.recv(1024)
    print(f"Received {response.decode()}")
        
def main():

    #Creating client socket connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("Connected to the server successfully!") 

    #Collecting user data after connection established
    id = input("Enter your ID: ").strip()
    firstName = input("Enter your first name: ").strip()
    lastName = input("Enter your last name: ").strip()
    userName = input("Enter your username: ").strip
    password = input("Enter your password: ").strip()
    userData =f"{id},{firstName},{lastName},{userName},{password}"

    # Send user data to server
    s.sendall(userData.encode())
    response = s.recv(1024)
    print(f"Received {response.decode()}")

    while True:
        #Creating command loop for the user to choose from
        command = input("Enter Command (BUY, SELL, BALANCE, LIST, SHUTDOWN, QUIT): ").strip().upper()
        if command in {"BUY", "SELL", "BALANCE", "LIST", "SHUTDOWN", "QUIT"}:
            sendCommand(s, command)
            if command == "QUIT":
                break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
