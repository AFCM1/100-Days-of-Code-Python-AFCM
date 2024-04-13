#My version - I sadly didn't use more complex conditions

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

my_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
my_choice = int(my_choice)
#print(type(my_choice))

if my_choice == 0:
  print(rock)
elif my_choice == 1:
  print(paper)
else:
  print(scissors)

computer_choice = random.randint(1, 3) #Wrong choice of range from me, should have used (0, 2), same range used in the my_choice input
#print(f"{computer_choice}")

print("Computer chose:\n")

if computer_choice == 1:
  print(rock)
elif computer_choice == 2:
  print(paper)
else:
  print(scissors)

if my_choice == 0: #I play rock
  if computer_choice == 1: #bot plays rock
    print("It\'s a draw")
  elif computer_choice == 2: #bot plays rock
    print("You win")
  else:
    print("You lose")

if my_choice == 1:           #I play paper
  if computer_choice == 1:   #bot plays rock
    print("You lose")
  elif computer_choice == 2: #bot plays paper
    print("It\s a draw")
  else:                      #bot plays scissors  
    print("You win")

if my_choice == 2:           #I play scissors
  if computer_choice == 1:   #bot plays rock
    print("You lose")
  elif computer_choice == 2: #bot plays paper
    print("You win")
  else:                      #bot plays scissors
    print("It\'s a draw")

#Angela version

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
