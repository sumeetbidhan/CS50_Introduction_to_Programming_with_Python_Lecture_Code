def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))


def square(n):
    #return n ** n
# another way of doing the same is
    return pow(n, 2)




main()