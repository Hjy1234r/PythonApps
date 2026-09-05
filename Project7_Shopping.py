# Shopping cart program

line_break="-"*36

while True:
    try:
        foods = []
        prices = []
        counts = []
        total = 0
        index = int(input("How many items will be in your cart? "))
        if index <= 0:
            print("The number cannot be negative or zero, please try again")
            print()
            continue

        for i in range(0, index):
            foods.append(input(f"What is your #{i+1} item? "))
            prices.append(float(input(f"What is the price ($) of your #{i+1} item? ")))
            counts.append(int(input("How many would you like? ")))
            total += prices[i]*counts[i]

        print("-------------YOUR CART-------------")

        for x in range(0, index):
            print(f"Item #{x+1}: {foods[x]} ${prices[x]:7,.2f} x{counts[x]}")

        print(line_break)
        print(f"Your total is ${total:7,.2f}")
        confirmation = input("Press Y to try again, any button to exit. ")
        if confirmation.lower().strip() == "y":
            print()
            continue
        break

    except ValueError:
        print("Wrong type of input value, please try again.")
        print(line_break)

