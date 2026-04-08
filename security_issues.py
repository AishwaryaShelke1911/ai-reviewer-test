import pickle
import subprocess
import os

# Security Issue 1: Insecure deserialization
def load_user_data(data):
    user = pickle.loads(data)  # VULNERABLE: pickle.loads with untrusted data
    return user

# Security Issue 2: SQL Injection
def get_user_by_name(name, db):
    query = f"SELECT * FROM users WHERE name = '{name}'"  # VULNERABLE: String interpolation
    return db.execute(query)

# Security Issue 3: Command Injection
def process_file(filename):
    os.system(f"cat {filename}")  # VULNERABLE: Command injection

# Security Issue 4: Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "admin123"

def connect_to_service():
    return {
        "api_key": API_KEY,
        "password": DB_PASSWORD
    }

# Security Issue 5: Use of eval
def evaluate_expression(user_input):
    result = eval(user_input)  # VULNERABLE: eval() on user input
    return result
# Another test
# Test update
# Final test
