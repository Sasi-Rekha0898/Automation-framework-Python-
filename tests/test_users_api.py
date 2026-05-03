import json

import pytest
from faker import Faker
from utils.api_utils import create_user, update_user, delete_user, get_users

fake = Faker()

@pytest.fixture(scope="module")
def create_user_fixture():
    payload = {
        "name": "Uttam",
        "email": fake.email(),
        "gender": "male",
        "status": "inactive"
    }

    response = create_user(payload)

    assert response.status_code == 201

    user = response.json()

    print("\nPOST RESPONSE:")
    print(json.dumps(user, indent=4))

    return user

def test_get_api():

    response = get_users()

    print("\nGET API SAMPLE (first 3 users):")
    print(json.dumps(response.json()[:3], indent=4))

    assert response.status_code == 200
    print("=================================================")


def test_put_api(create_user_fixture):

    user_id = create_user_fixture["id"]

    payload = {
        "name": "Uttam Updated",
        "email": fake.email(),
        "gender": "male",
        "status": "active"
    }

    response = update_user(user_id, payload)

    print("\nPUT RESPONSE:")
    print(json.dumps(response.json(), indent=4))

    assert response.status_code == 200
    assert response.json()["id"] == user_id
    print("=================================================")



def test_delete_api(create_user_fixture):

    user_id = create_user_fixture["id"]

    response = delete_user(user_id)

    print("\nDELETE RESPONSE:")
    print("Status Code:", response.status_code)

    assert response.status_code == 204
    print("=================================================")