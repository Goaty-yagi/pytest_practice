import pytest
import unittest.mock as mock
import requests

import source.service as service

# patch with path of the function you want to test


@mock.patch("source.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    # moch_get_user_from_db naming convention
    mock_get_user_from_db.return_value = "Mocked"
    user_name = service.get_user_from_db(1)

    assert user_name == "Mocked"


@mock.patch("requests.get")  # don't need to install?
def test_get_users(mock_get: mock.Mock):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Jphn Doe"}
    mock_get.return_value = mock_response
    data = service.get_users()
    assert data == {"id": 1, "name": "Jphn Doe"}
    mock_get.assert_called_once_with(
        'https://jsonplaceholder.typicode.com/users')


@mock.patch("requests.get")
def test_get_users_error(mock_get: mock.Mock):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
