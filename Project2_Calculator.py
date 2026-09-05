#Calculator
while True:
    op = input("Choose operation: ")
    a = float(input("Choose first number: "))
    b = float(input("Choose second number: "))

    if op == "+":
        print(f"Your result is {a + b}")
        break
    elif op == "-":
        print(f"Your result is {a - b}")
        break
    elif op == "*":
        print(f"Your result is {a * b}")
        break
    elif op == "/":
        print(f"Your result is {a / b}")
        break
    elif op == "**":
        print(f"Your result is {pow(a, b)}")
        break
    elif op == "%":
        print(f"Your result is {a % b}")
        break
    else:
        print(f"{op} is an invalid operator. Please try again.")

