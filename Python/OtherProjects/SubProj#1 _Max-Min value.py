#Find the max/min value from a set with n values.

error = "Wrong type of input. Please try again."

while True:
    op_type = input("Are you trying to find the MAX or MIN? ").lower().strip()
    if op_type == "max":
        stored_value = float("-inf")
        while True:
            try:
                value_count = int(input("Determine the number of values: "))
                if value_count <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                break
            except ValueError:
                print(error)

        for count in range(1, value_count + 1):
            while True:
                try:
                    value = float(input(f"Please type in the #{count} value: "))
                    if value > stored_value:
                        stored_value = value
                    break
                except ValueError:
                    print(error)
        break
    elif op_type == "min":
        stored_value = float("inf")
        while True:
            try:
                value_count = int(input("Determine the number of values: "))
                if value_count <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                break
            except ValueError:
                print(error)

        for count in range(1, value_count + 1):
            while True:
                try:
                    value = float(input(f"Please type in the #{count} value: "))
                    if value < stored_value:
                        stored_value = value
                    break
                except ValueError:
                    print(error)
        break
    else:
        print("Invalid operation. Please try again")
        continue

print (f"The {op_type} value is {stored_value}")

