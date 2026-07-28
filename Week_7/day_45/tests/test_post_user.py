from utils.api_client import *

def test_add_user():
    user_data = {
        "name": "BVNS",
        "username": "bvns",
        "email": "bvns@exp.com" 
        }

    response = post('users', payload = user_data)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"