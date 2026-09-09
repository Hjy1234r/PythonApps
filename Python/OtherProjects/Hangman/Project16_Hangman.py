# Hangman

import random
from Python.WordsHangman import words

# Dictionary
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
        }

def display_man(wrong_guesses):
    print("-------------")
    for printindex in range(3):
        print(hangman_art.get(wrong_guesses)[printindex])
    print("-------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    is_running = True
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while is_running:
        print()
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print()
            print("Invalid input.")
            continue

        elif guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            if wrong_guesses == 6:
                print()
                display_man(wrong_guesses)
                display_hint(answer)
                print("GAME OVER!")
                is_running = False
        
        if "_" not in hint:
            print()
            display_man(wrong_guesses)
            display_hint(hint)
            print("You Win!")
            is_running = False
        

if __name__ == '__main__':
    main()
