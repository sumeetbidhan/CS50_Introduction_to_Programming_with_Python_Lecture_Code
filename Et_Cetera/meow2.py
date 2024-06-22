import sys

if len(sys.argv) == 1:
    print("meows")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n int(sys.argv[2])
    for _ in range(n)
        print("meow")
else:
    print("usage: meows.py")