# Python quiz game

import annotationlib
question = ("Choose A",
            "Choose B",
            "Choose C",
            "Choose D",
            "Choose E")

options = (("A1", "B1", "C1", "D1"),
           ("A2", "B2", "C2", "D2"),
           ("A3", "B3", "C3", "D3"),
           ("A4", "B4", "C4", "D4"),
           ("A/5", "B/5", "C/5", "D/5"))

answers = ("A",
           "B",
           "C",
           "D",
           "E")

while True:
    input_user = []
    score = 0
    question_num = 0

    for ques_num in question:
        print(f"#{question_num + 1} {ques_num}")
        for index in options[question_num]:
            print(index)
        print()
        input_user.append(input("What is your answer? (A, B, C, D, or E): ").upper().strip())
        if input_user[question_num] not in ("A", "B", "C", "D", "E"):
            print("Invalid Answer.")
            break
        elif answers[question_num] == input_user[question_num]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {answers[question_num]}")
        question_num += 1
        
    if question_num < len(question):
        continue
    
    print("-------RESULTS-------")
    print("Answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print(f"\nGuesses: ", end="")
    for input1 in input_user:
        print(input1, end=" ")
    print()
    print(f"\nYour final score is {score} / {len(question)}pts")
    print("---------------------")
    confirmation = input("Press Y to try again, any button to exit. ")
    if confirmation.lower().strip() == "y":
        print()
        continue
    break
