from unittest.mock import Mock, patch

import pytest
import requests

from src.main import get_weather


@patch("src.main.requests.get")
def test_get_weather_success(mock_get):
    expected = {
        "name": "Hyderabad",
        "main": {"temp": 30},
    }

    response = Mock()
    response.json.return_value = expected
    response.raise_for_status.return_value = None
    mock_get.return_value = response

    result = get_weather("Hyderabad", "fake-test-key")

    assert result == expected
    assert mock_get.call_args.kwargs["params"]["q"] == "Hyderabad"
    assert mock_get.call_args.kwargs["params"]["units"] == "metric"


@patch("src.main.requests.get")
def test_get_weather_http_error(mock_get):
    mock_get.side_effect = requests.exceptions.HTTPError(
        "Request failed"
    )

    with pytest.raises(requests.exceptions.HTTPError):
        get_weather("Hyderabad", "fake-test-key")
