import requests
import pytest

URL = "http://reqres.in"

@pytest.fixture
def headers():
    return {"x-api-key":"reqres-free-v1"}


def test_get_users(headers):
    response = requests.get(URL + '/api/users?page=2', headers=headers)
    assert response.status_code == 200

def test_get_single_user(headers):
    response = requests.get(URL + "/api/users/2", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

def test_user_not_found(headers):
    response = requests.get(URL + "/api/users/23", headers=headers)
    assert response.status_code == 404