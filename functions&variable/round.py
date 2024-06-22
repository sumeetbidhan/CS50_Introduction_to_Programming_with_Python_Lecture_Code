# round(number[, ndigit])

x = float(input("What's x: "))
y = float(input("What's y: "))

z = round(x + y)
print(f"{z:,}")

# round till two values
#y = round(x / y, 2)
g = x / y
# another way of doing the same round till 2
print(f"{g:.2f}")