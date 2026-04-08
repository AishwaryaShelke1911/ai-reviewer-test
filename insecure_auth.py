import pickle

def deserialize_user(data):
    # Dangerous: pickle.loads() can execute arbitrary code
    return pickle.loads(data)

def verify_token(token):
    # No validation - accepts anything
    return True
