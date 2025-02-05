#Database connection
import sqlite3

db = sqlite3.connect('test.db')
print ("Opened database successfully")

#creating db table
db.execute('''CREATE TABLE Users
         (ID INT PRIMARY KEY AUTOINCREMENT,
         first_name           TEXT,
         last_name            TEXT,
         user_name        TEXT NOT NULL,
         password         TEXT,
         usd_balance DOUBLE NOT NULL);''')

db.execute('''CREATE TABLE Stocks
         (ID INT PRIMARY KEY AUTOINCREMENT,
         stock_symbol VARCHAR(4) NOT NULL,
         stock_name VARCHAR(20) NOT NULL,
         stock_balance DOUBLE,
         user_id INTEGER,
         FOREIGN KEY (user_id) REFERENCES Users (ID));''')


print ("Table created successfully")

db.close()