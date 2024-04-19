import os.path

files_dir = os.path.dirname(__file__)

def get_path(filename: str):
    return os.path.join(files_dir, filename)

csv_books = get_path(filename="books.csv")
json_user = get_path(filename="user.json")
json_result = get_path(filename="result.json")