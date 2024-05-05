import requests
from jsonschema import validate
import pytest


# posts
def test_json_schema_posts():
    # Выполняем GET-запрос к API
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Определяем ожидаемую структуру ответа
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": ["string", "null"]}
        },
        "required": [
            "userId",
            "id",
            "title",
            "body"
        ]
    }

    try:
        # Проверяем соответствие ответа ожидаемой схеме
        validate(instance=response.json(), schema=expected_schema)
    except Exception as e:
        assert False, f"JSON response does not match the expected schema: {e}"



# posts-comments http get типы данных
@pytest.mark.parametrize("num", ["1", "50", "100"])
def test_status_code_posts_comments(num):
    # Выполняем GET-запрос к API
    response = requests.get(f"http://jsonplaceholder.typicode.com/posts/{num}/comments")
    # Проверяем ответ через assert
    assert response.status_code == 200
    res_json = response.json()
    for comment in res_json:
        assert set(comment.keys()) == {'postId', 'id', 'name', 'email', 'body'}, \
            "Missing or unexpected keys in comment"
        assert isinstance(comment['postId'], int), "postId is not an integer"
        assert isinstance(comment['id'], int), "id is not an integer"
        assert isinstance(comment['name'], str), "name is not a string"
        assert isinstance(comment['email'], str), "email is not a string"
        assert isinstance(comment['body'], str), "body is not a string"

# albums_photos типы данных
@pytest.mark.parametrize("num", ["1", "50", "100"])
def test_status_code_albums_photos(num):
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums/{num}/photos")
    # Проверяем ответ через assert
    assert response.status_code == 200
    res_json = response.json()
    for photos in res_json:
        assert set(photos.keys()) == {'albumId', 'id', 'title', 'url', 'thumbnailUrl'}, \
            "Missing or unexpected keys in comment"
        assert isinstance(photos['albumId'], int), "postId is not an integer"
        assert isinstance(photos['id'], int), "id is not an integer"
        assert isinstance(photos['title'], str), "name is not a string"
        assert isinstance(photos['url'], str), "email is not a string"
        assert isinstance(photos['thumbnailUrl'], str), "body is not a string"

# posts-comments post
def test_json_schema_posts_post():
    # Выполняем GET-запрос к API
    response = requests.post('https://jsonplaceholder.typicode.com/posts',
                             data={'title': 'foo', 'body': 'bar', 'userId': 1})
    res_json = response.json()
    assert response.status_code == 201
    assert res_json['title'] == 'foo'
    assert res_json['body'] == 'bar'
    assert res_json['userId'] == '1'


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
