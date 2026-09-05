#Python Slot Machine

import random

def spin_row():
    symbols = ['🍉', '🍒', '🍊', '🍋', '⭐️']
    results = [random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    print("-"*10)
    print(" | ".join(row))
    print("-"*10)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*5
        elif row[0] == "🍉":
            return bet*3
        elif row[0] == "🍊":
            return bet*10
        elif row[0] == "🍋":
            return bet*14
        elif row[0] == "⭐️":
            return bet*21
    else:
        return 0

def main():
    balance = 100
    
    print("Welcome to Python Slots")
    print("Symbols: 🍉 🍒 🍊 🍋 ⭐️")

    while balance > 0:
        print(f"Current balance: ${balance:7,.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("Bet must be a positive number")
            continue

        balance -= bet
        
        print()
        row = spin_row()
        print_row(row)
        print()

        payout = get_payout(row, bet)

        if not payout > 0:
            print("You lost! Try again.")
        else:
            print(f"You won ${payout:5,.2f}")
            balance += payout

        play_again = input("Do you want to spin again? ").upper()

        if play_again != "Y":
            break

    print(f"Gamer over! Your final balance is ${balance:7,.2f}")


if __name__ == '__main__':
    main()