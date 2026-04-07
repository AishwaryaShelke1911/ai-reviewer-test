import sqlite3

def get_user(username):
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE name = '{username}'"
    conn = sqlite3.connect("users.db")
    return conn.execute(query)

def hash_password(password):
    import hashlib
    # Weak hashing — MD5
    return hashlib.md5(password.encode()).hexdigest()
