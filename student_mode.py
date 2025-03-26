#Student Mode

import json
flashcard = open("./flash_cards.json", encoding="utf8")
data = json.load(flashcard)

streak = 0
bonus_point = 0
question = 0
x = input("Do you want to take a small quiz for chemistry?")
if x.lower() == "yes":
    for properties in data:
        print(f"question:{properties['question']}")
        y = input("Answer:")
        if y.lower == (properties['answer']):
            print ("congraduation, it's correct.")
            streak = streak + 1
            bonus_point = bonus_point + 20
            question = question + 1
            if streak == 3:
                print("You are on fire! + 20")
                bonus_point = bonus_point + 20

                print(f"You have answered {question} questions and have a streak of {streak}. Total point = {bonus_point}")

            else:
                print("sorry, your answer is wrong.")
                return streak and bonus_point
                