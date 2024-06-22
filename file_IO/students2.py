import csv


students = []
with open("homes.csv") as file:
    reader = csv.DictReader(file)
    '''for row in reader:
        students.append({"name": row[0] , "home": row[1]})'''
    # another way of doing it is
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")