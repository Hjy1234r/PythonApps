import random

lowest_num = 1
highest_num = 100

target_int = random.randint(lowest_num, highest_num)

tries = 0

while True:
    try:
        guess = int(input(f"Make a guess ({lowest_num} to {highest_num}): "))
        if guess > highest_num or guess < lowest_num:
            print("Guess out of range.")
            continue
        tries +=1
        if guess > target_int:
            print("The number is lower!", end=" ")
        elif guess < target_int:
            print("The number is higher!", end=" ")
        if abs(guess - target_int) <=random.randint(4,7) and guess != target_int:
            print("Getting close!", end=" ")
        elif guess == target_int:
            print(f"You got it right in {tries} tries. The number is {target_int}!")
            confirmation = input("Press Y to try again, any button to exit. ")
            if confirmation.lower().strip() == "y":
                print()
                target_int = random.randint(lowest_num, highest_num)
                tries = 0
                continue
            break
    except ValueError:
        print("Only integers, please try again.")
        print()