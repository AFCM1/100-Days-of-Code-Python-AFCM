
####### Random module #######

import random
#import my_module
#print(my_module.pi)

# random_integer = random.randint(1, 10)
# print(random_integer)

# Generating float numbers #

# random_float = random.random()
# print(random_float)

# Generating float numbers 0 and 5#

# random_float = random.random()
# random_float *= 5
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

####### Python lists #######

# fruits = ["apple", "orange", "1", "true"]
# print(fruits[1])

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# states_of_america[1] = "Pencilvania" #Can modify an item in a list

# states_of_america.append("AFCMland") #Add an item at the end of a list
# states_of_america.extend(["item_added_1", "item_added_2"]) #Add several items at the end of a list

# states_of_america = random.choice(states_of_america)
# print(states_of_america)

####### IndexErrors and Working with Nested Lists #######

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

nb_states = len(states_of_america)
print(nb_states)

print(states_of_america[nb_states -1])


### Nested lists ###

fruits = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
