import json
import csv
from typing import List, Dict


class Merge_csv_json:

    def get_csv(self, path: str) -> List[Dict[str, any]]:
        """Метод для чтения данных из CSV файла и преобразования их в список словарей"""
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            return [
                {"title": value["Title"],
                 "author": value["Author"],
                 "pages": int(value["Pages"]),
                 "genre": value["Genre"]
                } for value in reader
            ]


    def get_json(self, path: str) -> List[Dict[str, any]]:
        """Метод для чтения данных из JSON файла и преобразования их в список словарей"""
        with open(path) as file:
            data = json.load(file)
            return [
                {"name": user_data["name"],
                 "gender": user_data["gender"],
                 "address": user_data["address"],
                 "age": user_data["age"]
                } for user_data in data
            ]


def distribute_books(users, books):
    """Функция для распределения книг пользователям"""
    num_users = len(users)
    books_per_user = len(books) // num_users
    extra_books = len(books) % num_users

    iter_books = iter(books)
    for user in users:
        user['books'] = []
        for _ in range(books_per_user):
            user['books'].append(next(iter_books))

        if extra_books > 0:
            user['books'].append(next(iter_books))
            extra_books -= 1

"""записываем данные в файл"""

def main():
    merge = Merge_csv_json()

    # Чтение данных из файлов
    users = merge.get_json('user.json')
    books = merge.get_csv('books.csv')

    # Распределение книг пользователям
    distribute_books(users, books)

    # Запись результатов в файл
    with open('result.json', 'w') as file:
        json.dump(users, file, indent=4)

if __name__ == "__main__":
    main()