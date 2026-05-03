import json
import requests
import pytest
from faker import Faker
fake = Faker()
base_url = "https://gorest.co.in"
auth = "Bearer 2cb4d5e41a2c2d75e06cb4dff67ddc1a7eb962c3e2b1498c0f3f563d7338007d"

@pytest.fixture()
def create_user():
    headers = {"Authorization": auth}
    url = base_url + "/public/v2/users"

    payload = {
        "name": "Uttam",
        "email": fake.email(),
        "gender": "male",
        "status": "inactive"
    }

    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 201

    user_id = response.json()["id"]
    return user_id


# ----------------- GET API -----------------
def test_get_api():
    headers = {"Authorization": auth}
    url = base_url + "/public/v2/users"

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))


# ----------------- POST API -----------------
def test_post_api():
    headers = {"Authorization": auth}
    url = base_url + "/public/v2/users"

    payload = {
        "name": "Uttam",
        "email": fake.email(),
        "gender": "male",
        "status": "inactive"
    }

    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 201
    print(json.dumps(response.json(), indent=4))


# ----------------- PUT API -----------------
def test_put_api(create_user):
    user_id = create_user

    headers = {"Authorization": auth}
    url = base_url + f"/public/v2/users/{user_id}"

    payload = {
        "name": "Uttam Updated",
        "email": fake.email(),
        "gender": "female",
        "status": "active"
    }

    response = requests.put(url, headers=headers, json=payload)

    assert response.status_code == 200
    print(json.dumps(response.json(), indent=4))


# ----------------- DELETE API -----------------
def test_delete_api(create_user):
    user_id = create_user

    headers = {"Authorization": auth}
    url = base_url + f"/public/v2/users/{user_id}"

    response = requests.delete(url, headers=headers)

    assert response.status_code == 204