from utils.api_client import *

def test_put_user():
    data = {
        "id" : 2,
        "name" : "Ervin Howell",
        "email" : "ervin.h@exp.com"
    }

    res = put('users/2', payload=data)
    assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}"
    assert data == res.json(), f"Expected data is {data} but got {res.json()}"
