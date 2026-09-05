import random

is_running = True
options = ("rock","paper","scissors")
user_choice = ""

while is_running:
    print()
    while user_choice not in options:
        user_choice = input("Rock Paper Scissors Shoot! ").strip().lower()

    bot_choice = random.choice(options)
    print()
    print(f"User:     {user_choice.capitalize()}")
    print(f"Computer: {bot_choice.capitalize()}")
    print()

    if bot_choice == user_choice:
        print("It's a tie!")
    elif bot_choice == "rock" and user_choice == "scissors":
        print("Computer wins")
    elif bot_choice == "scissors" and user_choice == "paper":
        print("Computer wins")
    elif bot_choice == "paper" and user_choice == "rock":
        print("Computer wins")
    else:
        print("User wins! Congrats.")
        print()

    confirmation = input("Press Y to try again, any button to exit. ")
    if confirmation.lower().strip() == "y":
        user_choice = ""
        print()
        continue
    is_running = False




    
