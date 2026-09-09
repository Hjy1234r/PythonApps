#Weight converter
while True:
    try:
        ic = input("Determine the input type (lbs, oz, kg, g): ").lower().strip()
        i = float(input("Determine the input weight according to the specified type: "))
        o = input("Determine the output type (lbs, oz, kg, g): ").lower().strip()
        break
    except ValueError:
        print("Please try again with correct value types.")


if ic == o:
    print("Error. Input and Output cannot be the same unit.")
else:
    #From kg
    if ic == "kg":
            if o == "g":
                print(f"Output: {round(i*1000, 4)} g")
            elif o == "lbs":
                print(f"Output: {round(i/0.45359237, 4)} lbs")
            elif o == "oz":
                print(f"Output: {round(i * 35.27392, 4)} oz")
            else:
                print("Error. Invalid output type.")
    #From lbs
    elif ic == "lbs":
            if o == "g":
                print(f"Output: {round(i*453.5924, 4)} g")
            elif o == "kg":
                print(f"Output: {round(i*0.45359237, 4)} kg")
            elif o == "oz":
                print(f"Output: {round(i * 16, 4)} oz")
            else:
                print("Error. Invalid output type.")
    #From g
    elif ic == "g":
            if o == "lbs":
                print(f"Output: {round(i/453.5924, 4)} lbs")
            elif o == "kg":
                print(f"Output: {round(i/1000, 4)} kg")
            elif o == "oz":
                print(f"Output: {round(i / 28.3495, 4)} oz")
            else:
                print("Error. Invalid output type.")
    #From oz
    elif ic == "oz":
            if o == "lbs":
                print(f"Output: {round(i/ 16, 4)} lbs")
            elif o == "kg":
                print(f"Output: {round(i/35.274, 4)} kg")
            elif o == "g":
                print(f"Output: {round(i * 28.3495, 4)} g")
            else:
                print("Error. Invalid output type.")
    else:
        print("Error. No valid conversion type.")










