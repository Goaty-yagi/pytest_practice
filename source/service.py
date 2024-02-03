import requests
from typing import Dict, Union

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}


def get_user_from_db(user_id: int) -> Dict[int, str]:
    return database.get(user_id)


def get_users() -> Union[Dict, None]:
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
