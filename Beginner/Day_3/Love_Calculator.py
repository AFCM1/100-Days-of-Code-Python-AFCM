print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
e1 = name1.count("e")
t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
e2 = name2.count("e")

l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
e1 = name1.count("e")
l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
e2 = name2.count("e")


truelove1 = int(t1 + r1 + u1 + e1 + t2 + r2 + u2 + e2) 
#print(truelove1)
truelove2 = int(l1 + o1 + v1 + e1 + l2 + o2+ v2 + e2)
#print(truelove2)
truelove1 = str(truelove1)
truelove2 = str(truelove2)
score = truelove1 + truelove2
#print("Your score is " + score)
score = int(score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

#Angela Version

#Notes : I should have combined both names into a single string and use the count function on it

# print("The Love Calculator is calculating your score...")
# name1 = input()  # What is your name?
# name2 = input()  # What is their name?
# # Your code below this line 👇
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# score = int(str(first_digit) + str(second_digit))
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
