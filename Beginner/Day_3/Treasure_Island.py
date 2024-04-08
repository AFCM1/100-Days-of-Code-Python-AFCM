path_1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right?"\n')
path_1 = path_1.lower()

if path_1 == "right":
  print("Game Over")
  exit()
if path_1 == "left":
  path_2 = input('You\'ve come to a lake. There is an island in the iddle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.\n')
path_2 = path_2.lower()
if path_2 == "swim":
  print("Game Over")
if path_2 == "wait":
  color = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
  color = color.lower()
  if color  == "red":
    print("It\'s a room full of fire. Game Over.")
  elif color == "blue":
    print("You enter a room of beasts. Game Over.")
  elif color == "yellow":
    print("You found the treasure! You Win!")
  else:
      print("You fell into a hole. Game Over.")

#Angela Version
#Notes : I'm using the lower function on a new line instead of using it on the same line than the input()
#Angela version is more readable + the indentation makes it clear for readability

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
