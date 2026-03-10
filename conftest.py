import pytest
from api_client.api_client import APIClient
from utils.config import BASE_URL, API_KEY
from utils.logger import get_logger


logger = get_logger(__name__)


@pytest.fixture(scope="session")
def api_client():

    if not API_KEY:
        pytest.skip("REQRES_API_KEY not set")

    logger.info("Initializing API Client")

    return APIClient(BASE_URL)