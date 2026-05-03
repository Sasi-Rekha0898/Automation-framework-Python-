import requests
from config.config_api import TOKEN, BASE_URL

HEADERS = {
    "Authorization": TOKEN
}

def create_user(payload):
    return requests.post(
        BASE_URL + "/public/v2/users",
        headers=HEADERS,
        json=payload
    )

def get_users():
    return requests.get(
        BASE_URL + "/public/v2/users",
        headers=HEADERS
    )

def delete_user(user_id):
    return requests.delete(
        BASE_URL + f"/public/v2/users/{user_id}",
        headers=HEADERS
    )

def update_user(user_id, payload):
    return requests.put(
        BASE_URL + f"/public/v2/users/{user_id}",
        headers=HEADERS,
        json=payload
    )