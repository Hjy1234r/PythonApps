import time
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}


number_of_dice = int(input("Enter the number of dice: "))
number_of_rolls = int(input("Enter the number of rolls for each dice: "))
total = 0
dice = []

for rolltimes in range(0, number_of_rolls):
    for die in range(0, number_of_dice):
        dice.append(random.randint(1,6))

    for counter in range(0, 5):
        for printindex in range(0, number_of_dice):
            print(dice_art.get(dice[printindex])[counter], end=" ")
        print()

    for value in dice:
        total += value
    
    dice = []
    time.sleep(1)


print(f"Your total is {total}.")
    







