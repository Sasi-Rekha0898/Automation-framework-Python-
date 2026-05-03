import requests
from config.config_api import TOKEN, BASE_URL

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}
def create_user(payload):
    return requests.post(
        BASE_URL + "/public/v2/users",
        headers=HEADERS,
        json=payload
    )


def get_users():
        response = requests.get(BASE_URL + "/public/v2/users", headers=HEADERS)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text[:200])
        return response

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