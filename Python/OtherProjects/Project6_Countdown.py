import time
while True:
    try:
        hours = int(input("Hour/s: "))
        minutes = int(input("Minute/s: "))
        seconds = int(input("Second/s: "))
        if hours < 0 or minutes < 0 or seconds < 0:
            print("Time cannot be negative")
            print("-"*32)
            continue
        elif hours > 24 or minutes > 60 or seconds > 60:
            print("The maximum is 24 hours or 60 minutes or 60 seconds. Please try again.")
            print("-" * 32)
            continue
    except ValueError:
        print("Invalid Input. Only integers are allowed.")
        print("-" * 32)
        continue
    time_seconds = hours * 3600 + minutes * 60 + seconds
    og_time = f"Alarm set for {hours:02} hour/s {minutes:02} minute/s {seconds:02} second/s"
    print(f"{og_time}.")
    print()

    for s in (range(0, time_seconds)):
        time.sleep(1)
        time_seconds -= 1
        print(f"\r{time_seconds//3600:02d}:{time_seconds//60 % 60:02d}:{time_seconds % 60:02d} remaining.", end="", flush=True)

    print()
    print("-" * 32)
    print(f"{og_time} is completed.")
    print("-" * 32)

    confirmation = input("Press Y to try again, any button to exit. ")
    if confirmation.lower().strip() == "y":
        print(" "*32)
        continue
    break
