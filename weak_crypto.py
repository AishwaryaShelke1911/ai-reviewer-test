import hashlib
import random

def generate_token():
    # Weak random - not cryptographically secure
    token = random.randint(0, 1000000)
    return str(token)

def hash_token(token):
    # Weak hashing
    return hashlib.sha1(token.encode()).hexdigest()
