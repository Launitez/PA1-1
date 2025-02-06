#Ilaun Baldwin-server implementation

import sqlite3

#creating server socket 
import socket
HOST = "127.0.0.1"
PORT = 3185

#creating database connection function
def createConnection(pa):
    conn = sqlite3.connect(pa)
    return conn
print ("Opened database successfully")

#creating db table if user does not exist automatically and setting balance to 100.00
def createUserTable(conn):
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        user_name TEXT NOT NULL,
        password TEXT,
        usd_balance DOUBLE NOT NULL DEFAULT 100.00
    )
    ''')
    conn.commit()

#inserting user data into the database
def insertUser(conn, id, first_name, last_name, user_name, password):
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Users (id, first_name, last_name, user_name, password) 
    VALUES (?, ?, ?, ?)
    ''', (id, first_name, last_name, user_name, password))
    conn.commit()

def handleClient(conn):
    db = createConnection('pa.db')
    createUserTable(db)
    
    with conn:
        userData = conn.recv(1024).decode()
        first_name, last_name, user_name, password = userData.split(',')
        insertUser(db, id, first_name, last_name, user_name, password)
        conn.sendall(b"User created successfully")
        
        while True:
            command = conn.recv(1024).decode()
            if not command:
                break
            print(f"Received command: {command}")
            
            if command == "QUIT":
                conn.sendall(b"Goodbye!")
                conn.close()
                break
            else:
                conn.sendall(b"Command received")
    
    db.close()
    print("Db Connection closed")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            handleClient(conn)

if __name__ == "__main__":
    main()
