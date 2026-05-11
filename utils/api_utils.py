import requests
from config.config_api import BASE_URL

HEADERS = {
    "Content-Type": "application/json",

}
def create_user(payload):
    return requests.post(
        f"{BASE_URL}/students",
        headers=HEADERS,
        json=payload
    )


def get_users():
        return requests.get(
            f"{BASE_URL}/students",
            headers=HEADERS
        )
def delete_user(user_id):
    return requests.delete(
        f"{BASE_URL}/students/{user_id}",
        headers=HEADERS
    )

def update_user(user_id, payload):
    return requests.put(
        f"{BASE_URL}/students/{user_id}",
        headers=HEADERS,
        json=payload
    )