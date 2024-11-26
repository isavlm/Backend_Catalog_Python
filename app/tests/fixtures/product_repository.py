import pytest
from pytest_mock import mocker


@pytest.fixture
def mock_product_repository(mocker):
    return mocker.MagicMock()
