import requests
from jsonschema import validate
import pytest
import json
from jsonschema.exceptions import ValidationError

with open('openbrewery_shemas.json', 'r') as file:
    schemas = json.load(file)

# List Breweries
def test_json_schema_list_breweries():
    # Выполняем GET-запрос к API
    response = requests.get('https://api.openbrewerydb.org/v1/breweries?per_page=3')
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['list_breweries_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    assert len(data) == 3


# List Breweries by_city
@pytest.mark.parametrize("city", ["san_diego", "mount_pleasant", "austin"])
def test_status_code_by_city(city):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=1")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['by_city_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    city_formatted = city.replace("_", " ")
    assert data[0]['city'].lower() == city_formatted


# List Breweries by_name
@pytest.mark.parametrize("name", ["san_diego", "eliot", "austin"])
def test_status_code_by_name(name):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_name={name}&per_page=1")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['by_name_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    city_formatted = name.replace("_", " ")
    assert data[0]['city'].lower() == city_formatted


# List Breweries by_state
@pytest.mark.parametrize("state", ["California", "Bouche du Rhône", "Colorado"])
def test_status_code_by_state(state):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_state={state}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['by_state_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    state_formatted = state.replace("_", " ").lower()
    assert data[0]['state'].lower() == state_formatted


# List Breweries by_type
@pytest.mark.parametrize("type", ["micro", "nano", "closed"])
def test_status_code_by_type(type):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_type={type}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['by_type_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)

    data = response.json()
    type_formatted = type.lower()
    assert data[0]['brewery_type'].lower() == type_formatted
