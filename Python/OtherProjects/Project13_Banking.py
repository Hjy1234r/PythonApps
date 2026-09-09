# Python Banking Program



is_running = True
current_balance = 0

def show_UI():
    print()
    print("-"*30)
    print(f"{"1. Show Balance":<30}")
    print(f"{"2. Deposit":<30}")
    print(f"{"3. Withdraw":<30}")
    print(f"{"4. Exit":<30}")
    print("-"*30)
    user_choiceUI(input(f"{"Choose action: ":>17}").strip().lower())

def balance(name):
    print("-------YOUR BALANCE-------")
    print(f"You have: ${name:10,.2f}")
    print()

def deposit():
    print("-------DEPOSIT-------")
    global current_balance
    inputuser = (input("How much would you like to deposit? "))
    if is_valid(inputuser):
        inputuser = float(inputuser)
        current_balance += inputuser
        print()
        print(f"Your deposit of ${inputuser:7,.2f} is successful!")
    else:
        print()
        print("Invalid input, please try again.")

def withdraw():
    print("-------WITHDRAW-------")
    global current_balance
    inputuser = input("How much would you like to withdraw? ")
    if is_valid(inputuser):
        if float(inputuser) > current_balance:
            print()
            print("Insufficient funds.")
        else:
            inputuser = float(inputuser)
            current_balance -= inputuser
            print()
            print(f"Your withdrawal of ${inputuser:7,.2f} is successful!")
    else:
        print()
        print("Invalid input, please try again.")


def is_valid(x):
    if x.isdigit():
        if float(x) >= 0:
            return True
        else:
            return False
    else: 
        return False

def user_choiceUI(x):
    match x:
        case "1" | "show balance" | "balance":
            return balance(current_balance)
        case "2" | "deposit":
            return deposit()
        case "3" | "withdraw":
            return withdraw()
        case "4" | "exit":
            print()
            print("Goodbye!")
            global is_running
            is_running = False
        case _:
            print ("Invalid choice, please try again.")
def main():            
    while is_running:
        show_UI()

if __name__ == '__main__':
    main()
        


