'''try:
    x = int(input("What's x?: "))

    print(f"x is {x}")
except ValueError:
    print("x is not a integer")
while True:
    try:
        x = int(input("What's x?: "))
    except ValueError:
        print("x is not a integer")
    else:
        break

print(f"x is {x}")'''

def main():
    x = get_int("What's X: ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass


if __name__ == '__main__':
    main()