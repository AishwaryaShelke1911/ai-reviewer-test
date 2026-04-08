import pickle
import subprocess

def load_user_data(data):
    """Load user data from pickle"""
    user = pickle.loads(data)  # VULNERABLE: pickle deserialization
    return user

def get_user_by_name(name, db):
    """Get user by name"""
    query = f"SELECT * FROM users WHERE name = '{name}'"  # VULNERABLE: SQL injection
    return db.execute(query)

def process_file(filename):
    """Process file"""
    os.system(f"cat {filename}")  # VULNERABLE: command injection

def connect_to_service():
    """Connect to service"""
    API_KEY = "sk-1234567890abcdef"  # VULNERABLE: hardcoded credentials
    return {"api_key": API_KEY}

def evaluate_expression(user_input):
    """Evaluate expression"""
    result = eval(user_input)  # VULNERABLE: eval on user input
    return result

