import pytest
import json
from jsonschema import validate

from api_client.api_client import APIClient
from utils.config import BASE_URL, API_KEY


@pytest.fixture
def api_client():
    if not API_KEY:
        pytest.skip("REQRES_API_KEY is not set")
    return APIClient(BASE_URL)


def load_schema():
    with open("schemas/user_schema.json") as f:
        return json.load(f)


def test_get_user(api_client):
    response = api_client.get("/users/2")

    assert response.status_code == 200

    data = response.json()

    validate(instance=data, schema=load_schema())


def test_create_user(api_client):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = api_client.post("/users", json=payload)

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == "morpheus"
    assert body["job"] == "leader"


def test_update_user(api_client):
    payload = {
        "name": "neo",
        "job": "the one"
    }

    response = api_client.put("/users/2", json=payload)

    assert response.status_code == 200


def test_delete_user(api_client):
    response = api_client.delete("/users/2")

    assert response.status_code == 204