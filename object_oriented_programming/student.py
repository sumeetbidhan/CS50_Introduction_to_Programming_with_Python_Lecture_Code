def main():

    #name, house = get_student()
    student = get_student()
    '''if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")'''
    if student["name"] == "Padma":
        student["house"] = "Rawenclaw"
    print(f"{student['name']} from {student['house']}")


'''def get_student():
    n = input("Name: ")
    h = input("House: ")
    #return n, h
    return [n, h]'''
'''def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student'''
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == '__main__':
    main()