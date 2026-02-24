import sqlite3

# Hardcoded credentials (security issue)
username = "admin"
password = "admin123"

def connect_db():
    conn = sqlite3.connect("users.db")
    return conn

def login(user_input, pass_input):
    conn = connect_db()
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + user_input + "' AND password = '" + pass_input + "'"
    cursor.execute(query)

    results = cursor.fetchall()

    if len(results) > 0:
        print("Login successful!")
    else:
        print("Login failed.")

    conn.close()

# No input validation
user = input("Enter username: ")
pw = input("Enter password: ")

login(user, pw)