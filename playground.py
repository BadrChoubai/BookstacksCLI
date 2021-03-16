import yaml
import csv
import os
from collections import defaultdict
from FileHandler import FileHandler


path = "bookstoadd.csv"

assert os.path.exists(path), "File not found at %s" % path

file_handler = FileHandler(path)
rows = file_handler.open()

_shelf = defaultdict(dict)
for q_name in ["WANT_TO_READ", "READING", "READ"]:
    _shelf[q_name] = defaultdict(list)

for row in rows:
    author, title, shelf = row[0], row[1], row[2]
    _shelf[shelf][author].append(title)


with open("./Books.yaml", "w") as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    book_list = yaml.dump(dict(_shelf), file)
