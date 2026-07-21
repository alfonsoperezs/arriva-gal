import requests
import pytest
from unittest.mock import Mock, patch


from arrivagal.api_client import APIClient


def test_api_client_get_success():
    mock_response = Mock()
    mock_response.json.return_value = {"test": "value"}

    with patch("requests.request", return_value=mock_response) as request:
        client = APIClient("https://api.test.com")

        result = client.get("/endpoint")

    assert result == {"test": "value"}
    request.assert_called_once_with(
        method="GET",
        url="https://api.test.com/endpoint"
    )


def test_api_client_request_error():
    with patch(
        "requests.request",
        side_effect=requests.RequestException("Connection error")
    ):
        client = APIClient("https://api.test.com")

        with pytest.raises(requests.RequestException):
            client.get("/endpoint")


def test_api_client_invalid_json():
    mock_response = Mock()
    mock_response.json.side_effect = ValueError("Invalid JSON")

    with patch("requests.request", return_value=mock_response):
        client = APIClient("https://api.test.com")

        with pytest.raises(ValueError):
            client.get("/endpoint")