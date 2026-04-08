import requests

def fetch_data(url):
    # No timeout - can hang indefinitely
    response = requests.get(url)
    return response.json()

def eval_expression(expr):
    # Dangerous: eval() can execute arbitrary code
    return eval(expr)
