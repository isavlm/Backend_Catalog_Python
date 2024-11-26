import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from api.src import create_app

@pytest.fixture(scope="module")
def app():
    return create_app()


@pytest.fixture(scope="module")
def client(app):
    return TestClient(app)


@pytest.fixture(scope="module")
def mock_session_manager():
    mock_session_manager = MagicMock()
    mock_session_manager.get_session.return_value = MagicMock()
    return mock_session_manager