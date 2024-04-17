import json
import csv
from typing import List, Dict

class Merge_csv_json:
    """читаем данные из csv и преобразуем их в список словарей"""
    def get_csv(self, path: str) -> List[Dict[str, any]]:
        """получаем структуру из CSV файла"""
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            return [
                {"title": value["Title"],
                 "author": value["Author"],
                 "pages": int(value["Pages"]),
                 "genre": value["Genre"]
                } for value in reader
            ]

    """читаем данные из json и преобразуем их в список словарей"""
    def get_json(self, path: str) -> List[Dict[str, any]]:
        """получаем структуру из JSON файла"""
        with open(path) as file:
            data = json.load(file)
            return [
                {"name": user_data["name"],
                 "gender": user_data["gender"],
                 "address": user_data["address"],
                 "age": user_data["age"]
                } for user_data in data
            ]
"""Итератор для списка книг"""
class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

"""распределяем книги"""
def distribute_books(users, books):
    """Распределяем книги"""
    book_iterator = BookIterator(books)
    num_users = len(users)

    for i, user in enumerate(users):
        user['books'] = []
        for a in range(len(books) // num_users):
            user['books'].append(next(book_iterator))

        if i < len(books) % num_users:
            user['books'].append(next(book_iterator))

"""записываем данные в файл"""
def write_json(data, file_path):
    merge = Merge_csv_json()

    reference_books = merge.get_json('user.json')

    filtered_data = []
    for entry in data:
        filtered_entry = {}
        for key in entry:
            if key in ['name', 'gender', 'address', 'age']:
                filtered_entry[key] = entry[key]
        filtered_data.append(filtered_entry)

    for user in filtered_data:
        user['books'] = reference_books

    with open(file_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)

def main():
    merge = Merge_csv_json()

    # Чтение данных из файлов
    users = merge.get_json('user.json')
    books = merge.get_csv('books.csv')

    # Распределение книг пользователям
    distribute_books(users, books)

    # Запись результатов в файл
    write_json(users, 'result.json')

main()