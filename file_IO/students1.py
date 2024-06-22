students = []

'''with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

print(students)
for students in sorted(students):
    print(students)'''

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        '''student = {}
        student["name"] = name
        student["house"] = house'''
        # or we can write the whole thing in just one line
        student = {"name": name, "house": house}
        students.append(student)

print(students)
print()
for student in students:
    print(f"{student['name']} is in {student['house']}")

print()
def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

print()

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_house,reverse=True):
    print(f"{student['name']} is in {student['house']}")

print()

for student in sorted(students, key = lambda student : student["name"]):
    print(f"{student['name']} is in {student['house']}")