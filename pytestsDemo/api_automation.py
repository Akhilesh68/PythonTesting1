import pytest
import requests
import json

# Key points
# json.dumps() converts json data into pretty json (easy to read)
# use command to run specific tests file: pytest  pytestsDemo/api_automation.py -v -s

base_url = "http://dummy.restapiexample.com"


@pytest.mark.skip
def test_get_request():
    url = base_url + "/api/v1/employees"
    print(f"get url: {url}")
    headers = {
        "User-Agent": "PostmanRuntime/7.26.10",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    # Status code validation
    assert response.status_code == 200
    print(f'GET API response code is: {response.status_code}')

    # Response body validation
    json_data = response.json()
    pretty_json = json.dumps(json_data, indent=4)
    print(f'json GET response body: {pretty_json}')
    assert "data" in json_data


# @pytest.mark.skip
def test_post_request():
    url = base_url + "/api/v1/create"
    print(f"post url: {url}")
    headers = {
        "User-Agent": "PostmanRuntime/7.26.10",
        "Accept": "application/json"
    }

    data = {
        "id": 30,
        "employee_name": "Akhilesh Patel",
        "employee_salary": "40000",
        "employee_age": "30"
    }

    response = requests.post(url, json=data, headers=headers)
    print(f'POST API response code is: {response.status_code}')
    assert response.status_code == 200  # Statsu code should be 201 (for POST Method) for creating data in server

    json_data = response.json()
    pretty_json = json.dumps(json_data, indent=2)
    print(f'json POST response body: {pretty_json}')
    assert "data" in json_data

    user_id = json_data['data']['id']
    print(f"User id: {user_id}")
    # assert "employee_name" in json_data
    assert json_data['data']['employee_name'] == 'Akhilesh Patel'

    return user_id  # we will use this id for PUT or DELETE method also to update or delete records of that specific user


# PUT method does not create new row in database,just update the records in server and database
def test_put_request(user_id):
    url = base_url + f"/api/v1/create/{user_id}"
    print(f"post url: {url}")
    headers = {
        "User-Agent": "PostmanRuntime/7.26.10",
        "Accept": "application/json"
    }

    data = {
        "id": 30,
        "employee_name": "Akhilesh Kumar Patel",
        "employee_salary": "60000",
        "employee_age": "28"
    }

    response = requests.put(url, json=data, headers=headers)
    print(f'PUT API response code is: {response.status_code}')
    assert response.status_code == 200
    json_data = response.json()
    pretty_json = json.dumps(json_data, indent=2)
    print(pretty_json)
