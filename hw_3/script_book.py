# импорт библиотек

import json
import csv

# Импорт адресов файлов?


# чтение данных из books.csv и приведение его в другой формат
def read_csv(file_path):
    data = [] # создаю пустой список
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row) # Записываю в список
    return data

# чтение данных из user.json и приведение его в другой формат. Через функцию или результат чтения в объект сохранять?
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file) # вернётся список из словарей

# Распределяем книги
# Создаю итератор
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

# Распределяю книги
def distribute_books(users, books):
    book_iterator = BookIterator(books)
    num_users = len(users)

    for i, user in enumerate(users):
        user['books'] = []
        for a in range(len(books) // num_users):
            user['books'].append(next(book_iterator))

        if i < len(books) % num_users:
            user['books'].append(next(book_iterator))


# записываем результаты в файл
def write_json(data, file_path):
    keys = list(data[0].keys()) if data else [] # определяем список ключей и если ключей нет то создаём пустой список

    with open('reference.json', 'r') as ref_file: #читаю файл reference.json и определяем список ключей в нём.
        reference_data = json.load(ref_file)
        reference_keys = list(reference_data[0].keys()) if reference_data else []

    filtered_data = []
    for entry in data:
        filtered_entry = {}
        for key in entry:
            if key in reference_keys:
                filtered_entry[key] = entry[key]
        filtered_data.append(filtered_entry)

    with open(file_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)

# Вызываем ранее созданные функции чтоб всё случилось

def main():
    # Чтение данных из файлов
    users = read_json('user.json')
    books = read_csv('books.csv')

    # Распределение книг пользователям
    distribute_books(users, books)

    # Запись результатов в файл
    write_json(users, 'result.json')

main()