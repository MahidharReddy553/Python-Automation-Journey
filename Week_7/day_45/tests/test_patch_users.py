from utils.api_client import *

def test_patch_user():
    data = {
        "email" : "ervin.h@exp.com"
    }

    res = patch('users/2', payload=data)
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"