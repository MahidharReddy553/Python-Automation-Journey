from utils.api_client import get


def test_users():
    response = get("users")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert len(response.json()) == 10, f"Expected 10 users, but got {len(response.json())}"

test_users()