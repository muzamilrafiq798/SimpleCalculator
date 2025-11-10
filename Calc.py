
def sum(a,b): return a+b

def sub(a, b): return a-b

def mul(a, b): return a*b

def div(a, b): return a/b if b!=0 else "Cannot divide by zero."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input")


while True:
    print("\n____SimpleCalculator____")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    op = input("Enter operation(+, -, *, /): ")

    if op.lower() == "q":
        print("Goodbye!")
        break


    if op == "+":
        print("Result: ", sum(a, b))

    elif op == "-":
        print("Result: ", sub(a, b))

    elif op == "*":
        print("Result: ", mul(a, b))

    elif op == "/":
        print("Result: ", div(a, b))

    else:
        print("Invalid operation")
