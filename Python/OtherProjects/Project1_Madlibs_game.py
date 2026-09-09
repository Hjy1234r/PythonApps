# Madlibs game
# Word game where you create a story.
# By filling in the blanks with random words.

while True:
    print(f"You are [BLANK] whose significant other [BLANK] was [BLANK].")
    print(f"As [BLANK] as you are right now, You can't help but [BLANK] about it.")

    character = input("Who are you? ")
    so = input("Who is your SO? ")
    word1 = input("What happened? ")
    adj1 = input("How are you feeling? ")
    verb1 = input("What are you doing here? ")
    confirmation = input("Are you sure? (YES/NO)")

    if confirmation.lower() == "yes":
        print(f"You are {character} whose significant other {so} was {word1}.")
        print(f"As {adj1} as you are right now, You can't help but {verb1} about it.")
        break
    else:
        print("REALLY? Try again")




