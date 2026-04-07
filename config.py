# Configuration file with security issue
import os

# Hardcoded password - security risk
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"

def load_config():
    # Missing input validation
    user_input = input("Enter username: ")
    return user_input
