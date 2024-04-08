names = names_string.split(", ")
# names_string contains the input values provided. 
# The code above converts the input into an array seperating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

# nb_items = len(names)
# print(nb_items)
# print(type(nb_items))
# print(names[0])
# print(names[-1])

random_name = names[random.randint(0, len(names)-1)]
print(f"{random_name} is going to buy the meal today!")

#Angela version

names = names_string.split(", ")

import random

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index. 
random_choice = random.randint(0, num_items - 1)
# Choose and print a random name.
print(names[random_choice])
