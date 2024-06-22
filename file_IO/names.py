'''names = []

for _ in range(3):
    name = input("What's your name?: ").title()
    names.append(name)
    #or we can simiply use names.append(input("What's your name?: ))

for name in sorted(names):
    print(f"hello, {name}")'''

#name = input("What's your name? ").title()
'''
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()'''

'''with open("names.txt", "a") as file:
    file.write(f"{name}\n")

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, ", line.rstrip())'''

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

'''with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())'''