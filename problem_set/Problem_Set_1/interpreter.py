'''x = int(input("Enter a number: "))
z = input("Choose an operator '+', '-', '*', '/': ")
y = int(input("Enter another number: "))

def calculator(a,b,c):
    if c == "+":
        return x + y
    elif c == "-":
        return x - y
    elif c == "*":
        return x * y
    elif c == "/":
        return x / y
    else:
        print("enter a valid input")


result = float(calculator(x,y,z))
print(result)
'''
expression = input("Expression: ")

x_str, operator, z_str = expression.split()

x = int(x_str)
z = int(z_str)

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        raise ValueError("Invalid operator")

result = calculator(x, z, operator)

print(f"{result:.1f}")

