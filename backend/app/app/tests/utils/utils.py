import random
import string

from fastapi.testclient import TestClient

from app.core.config import settings


# CODE = input('please input code to start the test:')
CODE = '001VXw1w3ewbRW29Zw1w3Ekpgf1VXw1C'  # TODO: 在此输入微信code

TOKEN = None


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"


def get_access_token(client: TestClient) -> str:
    global TOKEN
    if TOKEN:
        return TOKEN
    resp = client.get(f'{settings.CLASS_MANAGER_STR}/access_tokens/{CODE}')
    tokens = resp.json()
    assert resp.status_code == 200
    assert 'access_token' in tokens
    assert tokens['access_token']
    TOKEN = tokens['access_token']
    return TOKEN
