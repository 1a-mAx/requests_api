import pytest
import requests
import allure

@pytest.mark.description("Test retrieving a single user from the API.")
def test_single_user():
    with allure.step("Send GET request to retrieve a single user"):
        response = requests.get("https://reqres.in/api/users/2")
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        assert 'data' in response.json()
        assert response.json()['data']['id'] == 2

@pytest.mark.description("Test creating a new user with the API.")
def test_create_user():
    with allure.step("Prepare user data for creation"):
        user_data = {
            "name": "morpheus",
            "job": "leader"
        }
    with allure.step("Send POST request to create a new user"):
        response = requests.post("https://reqres.in/api/users", json=user_data)
        assert response.status_code == 201
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        response_json = response.json()
        assert 'id' in response_json
        assert response_json['name'] == user_data['name']
        assert response_json['job'] == user_data['job']

@pytest.mark.description("Test updating a user with the API.")
def test_update_user():
    with allure.step("Prepare updated user data"):
        user_data = {
            "name": "morpheus",
            "job": "zion resident"
        }
    with allure.step("Send PUT request to update the user"):
        response = requests.put("https://reqres.in/api/users/2", json=user_data)
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
        response_json = response.json()
        assert response_json['name'] == user_data['name']
        assert response_json['job'] == user_data['job']

@pytest.mark.description("Test deleting a user with the API.")
def test_delete_user():
    with allure.step("Send DELETE request to remove the user"):
        response = requests.delete("https://reqres.in/api/users/2")
        assert response.status_code == 204
        assert response.text == ''
