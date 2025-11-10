from operator import truediv

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation(+, -, *, /): ")

def sum(a,b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def get_number(a, b):
    while(True):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input")

if op == "+":
    print(sum(a, b))

elif op == "-":
    print(sub(a, b))

elif op == "*":
    print(mul(a, b))

elif op == "/":
    print(div(a, b))

else:
    print("Invalid operation")
