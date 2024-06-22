students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russle terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for x in students:
    print(x["name"], x["house"],x["patronus"], sep=", ")