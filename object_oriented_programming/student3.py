class Student:
    def __init__(self, name, house, patronous):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house
        self.patronous = patronous

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronous:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    print(student)  # Prints the student's name and house
    print("Expecto Patronum!")
    print(student.charm())  # Prints the corresponding emoji for the patronous

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronous = input("Patronous: ")
    return Student(name, house, patronous)

if __name__ == '__main__':
    main()
