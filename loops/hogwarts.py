'''students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


print(students[0])
print(students[1])
print(students[2])


for student in students:
    print(student)

print()

for i in range(len(students)):
    print(i, students[i])'''

students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }
for student in students:
    print(student, students[student], sep=", ")

