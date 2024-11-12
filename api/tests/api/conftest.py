import pytest
from fastapi.testclient import TestClient

from api.src.create_app import create_app


@pytest.fixture
def api_client() -> TestClient:
    api = create_app()
    client = TestClient(api)

    return client
