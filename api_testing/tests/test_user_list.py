from api_testing.api_data.api_test_data import payload, StatusCodes
from api_testing.utils.assertions import assert_status_code


def test_get_users(users_api):
    response = users_api.get_users(page=1)

    assert_status_code(response=response, expected=StatusCodes.OK)
    data = response.json()

    assert "data" in data
    assert len(data["data"]) > 0

def test_get_single_user(users_api):
    response = users_api.get_user(user_id=2)
    assert_status_code(response=response, expected=StatusCodes.OK)
    assert response.json()["data"]["id"] == 2

def test_create_user(users_api):
    response = users_api.create_user(payload=payload)

    assert_status_code(response=response,expected=StatusCodes.Created)

    body = response.json()

    assert body["name"] == "Nichasius"
    assert "id" in body

def test_delete_user(users_api):
    response = users_api.delete_user(payload=payload)
    assert_status_code(response=response,expected=StatusCodes.Deleted)
