import requests
from jsonschema import validate
import pytest
import json
from jsonschema.exceptions import ValidationError

with open('jsonplaceholder_schemas.json', 'r') as file:
    schemas = json.load(file)
# posts
def test_json_schema_posts():
    # Выполняем GET-запрос к API
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['posts_schema'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    assert data["body"] is not None or data["body"] == ""



# posts-comments http get типы данных
@pytest.mark.parametrize("num", ["1", "50", "100"])
def test_status_code_posts_comments(num):
    # Выполняем GET-запрос к API
    response = requests.get(f"http://jsonplaceholder.typicode.com/posts/{num}/comments")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['posts_comment'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    assert len(data) > 0



# albums_photos типы данных
@pytest.mark.parametrize("num", ["1", "50", "100"])
def test_status_code_albums_photos(num):
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums/{num}/photos")
    # Проверяем ответ через assert
    assert response.status_code == 200
    try:
        validate(instance=response.json(), schema=schemas['albums_photos'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    data = response.json()
    assert len(data) > 0


# posts-comments post
def test_json_schema_posts_post():
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             data={'title': 'foo', 'body': 'bar', 'userId': 1})
    assert response.status_code == 201
    try:
        validate(instance=response.json(), schema=schemas['posts_post'])
    except ValidationError as e:
        print("JSON response does not match the expected schema:", e)
    res_json = response.json()
    assert res_json['title'] == 'foo'


# posts-comments put
@pytest.mark.xfail(strict=True)
def test_json_schema_posts_put():
    # Выполняем post-запрос на создание объекта который будем затем редактировать
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             data={'title': 'boo', 'body': 'bar', 'userId': 2})
    res_json = response.json()
    post_id = res_json['id']
    # Формируем put запрос
    put_url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    # Выполняем put-запрос меняем title
    response = requests.put(put_url, data={"title": "too"})
    res_json = response.json()
    assert response.status_code == 200

    assert res_json['title'] == 'too'
# оказывается я не могу поменять только что созданный пост №101 приходит ошибка серввера 500
