import requests
from jsonschema import validate
import pytest


# Random image
def test_json_schema_random_image():
    # Выполняем GET-запрос к API
    response = requests.get('https://dog.ceo/api/breeds/image/random')

    # Определяем ожидаемую структуру ответа
    expected_schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    # Проверяем соответствие ответа ожидаемой схеме
    validate(instance=response.json(), schema=expected_schema)


# By breed
@pytest.mark.parametrize("breed", ["chihuahua", "poodle", "labrador"])
def test_status_code_by_breed(breed):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images")
    # Проверяем ответ через assert
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0
    message = response.json().get("message", [])
    for i in message:
        assert breed in i


# By sub-breed

@pytest.mark.parametrize("breed", ["retriever", "poodle", "ridgeback"])
def test_status_code_by_sub_breed(breed):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/list")
    # Проверяем ответ через assert
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0


# List all breeds
def test_json_schema_list_all_breeds():
    # Выполняем GET-запрос к API
    response = requests.get('https://dog.ceo/api/breeds/list/all')

    # Определяем ожидаемую структуру ответа
    expected_schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"}
        },
        "required": ["message", "status"]
    }

    # Проверяем соответствие ответа ожидаемой схеме
    validate(instance=response.json(), schema=expected_schema)


# Browse breed list
@pytest.mark.parametrize("breed", ["chihuahua", "poodle", "labrador"])
def test_status_code_breed_list(breed):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    # Проверяем ответ через assert
    assert response.status_code == 200
    assert len(response.json()["message"]) > 0
