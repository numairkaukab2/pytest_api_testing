import requests

URL = "http://reqres.in"

def test_get_users():
    response = requests.get(URL + '/api/users?page=2')
    assert response.status_code == 200
    