import random

game = {"R":"red","Y":"yellow","G": "green", "B": "Blue", "I":"Indigo", "V": "Violet"}

keys = list(game)
color = random.sample(list(game),4)
print(color)