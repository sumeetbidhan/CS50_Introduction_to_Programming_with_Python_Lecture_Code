students = [
    {"name": "Hermoine", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},

]


'''def is_gryffindor(s):
    if s["house"] == "Gryffindor":
        return True
    else:
        return False'''

'''def is_gryffindor(s):
    return s["house"] == "Gryffindor" '''

#gryffindors = filter(is_gryffindor, students)

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])