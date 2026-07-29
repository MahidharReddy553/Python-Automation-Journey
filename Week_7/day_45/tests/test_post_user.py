from utils.api_client import *

def test_add_user():
    user_data = {
        "name": "BVNS",
        "username": "bvns",
        "email": "bvns@exp.com" 
        }

    response = post('users', payload = user_data)

    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"


def test_negative_post_user():

    user_data = {
        "email" : 'invalid-email'
    }

    res = post('users/1', payload = user_data)
    print(res.status_code)
    assert res.status_code == 404, f"Expected status code 404, but got {res.status_code}"