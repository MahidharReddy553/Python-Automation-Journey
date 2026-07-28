import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get(endpoint, params = None):
    return requests.get(f"{BASE_URL}/{endpoint}", params = params)

def post(endpoint, payload = None):
    return requests.post(f"{BASE_URL}/{endpoint}", json=payload)

def put(endpoint, payload):
    return requests.put(f"{BASE_URL}/{endpoint}", data=payload)

def patch(endpoint, payload):
    return requests.patch(f"{BASE_URL}/{endpoint}", data=payload)

def delete(endpoint):
    return requests.delete(f"{BASE_URL}/{endpoint}")
