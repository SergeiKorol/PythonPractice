# импорт библиотек

import json
import csv
from csv import DictReader

# Импорт адресов файлов?


# чтение данных из books.csv и приведение его в другой формат
def read_csv(file_path):
    data = [] # создаю пустой список
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row) # Записываю в список
    return data

books = read_csv('books.csv')
print(books)

# чтение данных из user.json и приведение его в другой формат. Через функцию или результат чтения в объект сохранять?
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file) # вернётся список из словарей

users = read_json('user.json')
print(users)

# Распределяем книги
books = read_csv('books.csv')
users = read_json('user.json')

total_user = len(users)
total_books = len(books)

print(total_user)
print(total_books)

# записываем результаты в файл

# Вызываем ранее созданные функции чтоб всё случилось