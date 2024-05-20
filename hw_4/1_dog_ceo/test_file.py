import requests
from jsonschema import validate
import pytest
import json

with open('dog_api_shemas.json', 'r') as file:
    schemas = json.load(file)

# Random image
def test_json_schema_random_image():
    # Выполняем GET-запрос к API
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    assert response.status_code == 200
    # Проверяем соответствие ответа ожидаемой схеме
    validate(instance=response.json(), schema=schemas['random_image_schema'])
    assert len(response.json()["message"]) > 0


# By breed
@pytest.mark.parametrize("breed", ["chihuahua", "poodle", "labrador"])
def test_status_code_by_breed(breed):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images")
    # Проверяем ответ через assert
    assert response.status_code == 200
    validate(instance=response.json(), schema=schemas['by_breed_schema'])
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
    validate(instance=response.json(), schema=schemas['by_sub_breed_schema'])
    assert len(response.json()["message"]) > 0


# List all breeds
def test_json_schema_list_all_breeds():
    # Выполняем GET-запрос к API
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200
    # Проверяем соответствие ответа ожидаемой схеме
    validate(instance=response.json(), schema=schemas['list_all_breeds_schema'])
    assert len(response.json()["message"]) > 0


# Browse breed list
@pytest.mark.parametrize("breed", ["chihuahua", "poodle", "labrador"])
def test_status_code_breed_list(breed):
    # Выполняем GET-запрос к API
    response = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    # Проверяем ответ через assert
    assert response.status_code == 200
    validate(instance=response.json(), schema=schemas['breed_list'])
    assert len(response.json()["message"]) > 0
