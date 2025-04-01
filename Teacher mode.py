# You will be creating an application that has two modes. You will leverage
# classes in Python to accomplish the tasks. You will be penalized for
# unnecessary code if you replicate features that already exist in Python.

# Teacher Mode

# In teacher mode you will be asking the user to input a word/phrase and the
# answer as a key:value pair. You can also attach an image. These pairs will
# be written to a json file called FlashCards.json.

# Student Mode
# In student mode you will present the student with the
# phrases/words/images and the user will type the answer in the terminal.
# Keep a tally of correct answers and provide a score. Give students bonus
# points for “Streaks.

# import json 
# from PIL import Image
# def cards():
#     try:
#         with open("flash_cards.json", "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []
# flashcards = cards()
# class flash_cards:
#     def __init__(self, question, answer, image_path=None):
#         self.question = question
#         self.answer = answer
#         self.image_path = image_path

#     def display_info(self):
#         return f"{self.question}    {self.answer}"
        
    # def show_image(self):
    #     if self.image_path:
    #         try:
    #             img = Image.open(self.image_path)
    #             img.show()
    #         except FileNotFoundError:
    #             print("Error: Image file not found.")

# Flash_cards = [
#    Card("What is the atomic number of carbon?","6")
#    Card("What is the pH of neutral water?", "7")
#    Card("What gas do plants absorb during photosynthesis?", "CO2")
#    Card("What is the main component of natural gas?", "Methane")
#    ]
# cards_data = [card.to_dict() for card in cards]
# with open("cards.json", "w") as file:
#     json.dump(cards_data, file, indent=4)

# new_card = Card("What is the chemical symbol for water?", "H2O")




# class calculator():
#     def add(x, y):
#         print(x + y)
#         return x + y
#     def add_many(list):
#         print(sum(list))
#         return sum(list)
#     def subtract(list):
#         return list
    



# class Merchant:
#     def __init__(self, name, products):
#         self.name = name
#         self.products = products
#     def sell(self, item):
#         self.products.remove(item)
#         print(self.products)
# Joanna = Merchant("Joanna", ['chicken', 'pork', 'beef'])
# Joanna.sell('pork')
# Alvin = Merchant("Alvin", ["Human", "Alvin's Servitude", "Breaks", "Organs"])
# Alvin.sell("Organs")


# [
#    
#     {"Question" :"What is the atomic number of carbon?",
#     "Answer" :"6"},
#     {"Question" :"What is the pH of neutral water?",
#     "Answer" :"7"},
#     {"Question" :"What gas do plants absorb during photosynthesis?",
#     "Answer" :"CO2"},
#     {"Question" :"What is the main component of natural gas?",
#     "Answer" :"Methane"},
#     {"Question" :"What element has the symbol 'Na'?",
#     "Answer" :"Sodium"}
# ]

#Teacher Mode
import json
print("Add questions and answers in the new_card section to be upload to json.")
class Flashcards:
    def __init__(self, question, answer, image_path=None):
        self.question = question
        self.answer = answer
        self.image_path = image_path

    def display_info(self):
        return f"{self.question}    {self.answer}"
    
    def to_dict(self):
        return{
            "question": self.question,
            "answer": self.answer,
            "image_path": self.image_path
        }
flash_cards = [
   Flashcards("What is the atomic number of carbon?","six"),
   Flashcards("What is the pH of neutral water?", "seven"),
   Flashcards("What gas do plants absorb during photosynthesis?", "co2"),
   Flashcards("What is the main component of natural gas?", "Methane")
   ]
cards_data = [card.to_dict() for card in flash_cards]
with open("flash_cards.json", "w") as file:
    json.dump(cards_data, file, indent=4)

new_card = Flashcards("What is the chemical symbol for water?", "h2o")

try:
    with open("flash_cards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    
    cards_data = []
cards_data.append(new_card.to_dict())

with open("flash_cards.json", "w") as file:
    json.dump(cards_data, file, indent=4)

print("It's been added to json.")

