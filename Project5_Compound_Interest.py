#Python compound interest calculator
while True:
    try:
        initial_balance = float(input("Your initial deposit (USD): "))
        interest_rate = float(input("The interest rate (percent): "))
        time_period = int(input("How long it has been since your deposit (years): "))
        if initial_balance <= 0 or interest_rate <= 0 or time_period <= 0:
            print("Values can't be negative or zero. Please try again. ")
            print("-"*30)
            continue
        initial_balance = initial_balance * pow((1 + interest_rate / 100), time_period)
        print("-" * 30)
        print(f"Your final balance after {time_period} year(s) is ${initial_balance:7,.2f}")
        print("-" * 30)
        confirmation = input("Press Y to try again, any button to exit. ")
        if confirmation.lower().strip() == "y":
            continue
        break
    except ValueError:
        print("Wrong type of value. Please try again.")
        print("-" * 30)
        continue



