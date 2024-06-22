import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        #house = random.choice(cls.houses)
        #print(name, "is in", house)
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")