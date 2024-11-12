from http import HTTPStatus

from fastapi.testclient import TestClient


def test__returns_ok_status__when_api_is_working_correctly(api_client: TestClient):
    response = api_client.get("/health_check/")

    response_content = response.json()
    assert response.status_code == HTTPStatus.OK
    assert response_content["status"] == "OK"
