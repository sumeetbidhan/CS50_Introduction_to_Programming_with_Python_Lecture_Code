import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    def sort(self, name):
        #house = random.choice(self.houses)
        #print(name, "is in", house)
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")