#Concession stand program

menu = {"Pizza": 10.99,
        "Nachos": 4.50,
        "Fries": 3.50,
        "Soda": 0.99,
        "Chips": 4.99,
        "Lemonade": 1.99}

cart = []
number = []
total = 0

print("-------Menu-------")

for key, value in menu.items():
    print(f"{key:10}: ${value:5.2f}")

print("------------------")

while True:
    cart.append(input("What would you like? (N to quit) ").lower().capitalize().strip())
    if cart[-1] == "N":
        cart.pop(-1)
        break
    number.append(int(input("How many of it would you like? ")))
    total += menu.get(cart[-1]) * number[-1]
print()
print("Your order is:")
for index in range(len(cart)):
    print(f"{number[index]}x {cart[index]}")
print(f"The total is ${total:.2f}")


