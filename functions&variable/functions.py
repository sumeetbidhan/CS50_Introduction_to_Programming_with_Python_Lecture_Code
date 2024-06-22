
def main():
    hello()
    name = input("what's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()