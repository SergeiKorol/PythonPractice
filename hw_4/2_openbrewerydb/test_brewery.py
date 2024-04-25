import requests
from jsonschema import validate
import pytest


# List Breweries
def test_json_schema_list_breweries():
    # Выполняем GET-запрос к API
    response = requests.get('https://api.openbrewerydb.org/v1/breweries?per_page=3')

    # Определяем ожидаемую структуру ответа
    expected_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "name": {"type": "string"},
                "brewery_type": {"type": "string"},
                "address_1": {"type": ["string", "null"]},
                "address_2": {"type": ["string", "null"]},
                "address_3": {"type": ["string", "null"]},
                "city": {"type": "string"},
                "state_province": {"type": "string"},
                "postal_code": {"type": "string"},
                "country": {"type": "string"},
                "longitude": {"type": ["string", "null"]},
                "latitude": {"type": ["string", "null"]},
                "phone": {"type": ["string", "null"]},
                "website_url": {"type": ["string", "null"]},
                "state": {"type": ["string", "null"]},
                "street": {"type": ["string", "null"]}
            },
            "required": [
                "id",
                "name",
                "brewery_type",
                "city",
                "state_province",
                "postal_code",
                "country",
                "longitude",
                "latitude",
                "state",
                "street"
            ]
        }
    }

    try:
        # Проверяем соответствие ответа ожидаемой схеме
        validate(instance=response.json(), schema=expected_schema)
    except Exception as e:
        assert False, f"JSON response does not match the expected schema: {e}"


# List Breweries by_city
@pytest.mark.parametrize("city", ["san_diego", "mount_pleasant", "austin"])
def test_status_code_by_city(city):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200


# List Breweries by_name
@pytest.mark.parametrize("name", ["san_diego", "mount_pleasant", "austin"])
def test_status_code_by_name(name):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_name={name}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200


# List Breweries by_state
@pytest.mark.parametrize("state", ["California", "Bouche du Rhône", "Colorado"])
def test_status_code_by_state(state):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_state={state}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200


# List Breweries by_type
@pytest.mark.parametrize("type", ["micro", "nano", "closed"])
def test_status_code_by_type(type):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://api.openbrewerydb.org/v1/breweries?by_type={type}&per_page=3")
    # Проверяем ответ через assert
    assert response.status_code == 200
