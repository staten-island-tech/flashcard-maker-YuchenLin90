#Student Mode
# In student mode you will present the student with the
# phrases/words/images and the user will type the answer in the terminal.
# Keep a tally of correct answers and provide a score. Give students bonus
# points for “Streaks.
import json
from PIL import Image

with open("./flash_cards.json", encoding="utf8") as flashcard:
    data = json.load(flashcard)

streak = 0
bonus_point = 0
question = 0

x = input("Do you want to take a small quiz for chemistry?")
if x.lower() == "yes":
    for properties in data:
        print(f"question:{properties['question']}")
        
        image_path = properties.get("image_path") 
         
        if image_path:
            try:
                img = Image.open(image_path)
                img.show()
            except FileNotFoundError:
                print(f"Image not found: {image_path}")
        y = input("Answer:")

        if y.lower()== properties['answer'].lower():
            print ("congraduation, it's correct.")
            streak = streak + 1
            bonus_point = bonus_point + 20
            question = question + 1

            if streak == 3:
                print("You are on fire! + 20")
                bonus_point = bonus_point + 20
        else:
            print("Sorry, you are wrong.")
            break
            
print(f"You have answered {question} questions and have a streak of {streak}. Total point = {bonus_point}")
