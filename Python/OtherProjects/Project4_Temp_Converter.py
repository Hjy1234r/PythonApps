#Temperature Converter
while True:
    try:
        input_temp = float(input("Input Temperature: "))
        break
    except ValueError:
        print("Only numbers are allowed in the field.")

input_type = input("Determine the Input type (C, K, F): ").lower().strip()
output_type = input("Determine the Output type (C, K, F): ").lower().strip()

if input_type == output_type:
    print("Input and Output cannot be in the same unit.")
elif input_type == "c":
    if output_type == "k":
        print(f"Output Temperature: {round(input_temp + 273.15, 4)} Kelvin")
    elif output_type == "f":
        print(f"Output Temperature: {round(input_temp*1.8 + 32, 4)} Fahrenheit")
    else:
        print("Error: Invalid output type.")
elif input_type == "k":
    if output_type == "c":
        print(f"Output Temperature: {round(input_temp - 273.15, 4)} Celsius")
    elif output_type == "f":
        print(f"Output Temperature: {round((input_temp - 273.15)*1.8 + 32, 4)} Fahrenheit")
    else:
        print("Error: Invalid output type.")
elif input_type == "f":
    if output_type == "c":
        print(f"Output Temperature: {round((input_temp - 32)/1.8, 4)} Celsius")
    elif output_type == "k":
        print(f"Output Temperature: {round((input_temp - 32)/1.8 + 273.15, 4)} Kelvin")
    else:
        print("Error: Invalid output type.")
else:
    print("Invalid Conversion Type.")







