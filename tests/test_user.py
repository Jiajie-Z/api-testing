import pytest
import json

from api_client.api_client import APIClient
from utils.config import BASE_URL, API_KEY
from utils.response_validator import validate_schema
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.fixture
def api_client():

    if not API_KEY:
        pytest.skip("REQRES_API_KEY not set")

    return APIClient(BASE_URL)


def load_test_data():

    with open("test_data/users.json") as f:
        return json.load(f)


def test_get_user(api_client):

    logger.info("Testing GET /users/2")

    response = api_client.get("/users/2")

    assert response.status_code == 200

    validate_schema(
        response.json(),
        "schemas/user_schema.json"
    )


def test_create_user(api_client):

    data = load_test_data()["create_user"]

    response = api_client.post(
        "/users",
        json=data
    )

    assert response.status_code == 201

    body = response.json()

    assert body["name"] == data["name"]
    assert body["job"] == data["job"]


def test_update_user(api_client):

    data = load_test_data()["update_user"]

    response = api_client.put(
        "/users/2",
        json=data
    )

    assert response.status_code == 200


def test_delete_user(api_client):

    response = api_client.delete("/users/2")

    assert response.status_code == 204