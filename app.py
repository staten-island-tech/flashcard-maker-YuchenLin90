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

import json 
try:
    with open("flash_cards.json") as file:
        flashcards = json.load(file)
except FileNotFoundError:
    flashcards = []

class flash_cards:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_info(self):
        return f"{self.question}    {self.answer}"
        



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


