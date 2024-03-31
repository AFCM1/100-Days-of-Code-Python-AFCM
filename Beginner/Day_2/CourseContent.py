###### Data Types ######


#"Hello" - String
# 123 456 - Integer - Positive or negative numbers with no decimals
# 123.45 - Float - Floating point number
# True or False - Boolean


###### Data Types Functions ######

# num_char = len(input("What\'s your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters")
#print(type(num_char))

# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# print(str(70) + str(200))

########################################################################
## Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

# digit1 = int(two_digit_number[0])
# digit2 = int(two_digit_number[1])

# print(digit1 + digit2)

###### Mathematical Operations in Python ######

# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# (2 ** 3)

# PEMDAS PRIORITY

# Parentheses ()
# Exponents **
# Multiplication *  Division /
# Addition Substraction

# print(3 * 3 + 3 / 3 - 3)
# 9 + 1 - 3 = 7

#Change so we have 3 as result

# print(3 * (3 + 3) / 3 - 3)
########################################################################
###### BMI Calculator ######

# 1st input: enter height in meters e.g: 1.65
# height = input()
# 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# height2 = float(height)
# weight2 = int(weight)
# BMI = weight2 / (height2 * height2)
# print(int(BMI))

###### Number Manipulation and fStrings ######

# print(round(8 / 3, 3))

# print(type(4 / 2))
#float

# print(type(4 // 2))
#int

# result = 4 / 2
# result /= 2
# print(result)


# score = 0
#User scores a point
# height = 1.8
# isWinning = True

#f-String
#print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
#print("Your score is " + str(score))

########################################################################
# Create a program using maths 
# and f-Strings that tells us how many weeks we have left
# if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

#age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# age2 = int(age)
# years_left = age2 - 90
# weeks_now = age2 * 52
#print(f"You had lived {weeks_now} weeks until now")
# weeks_left = 4680 - weeks_now
# print(f"You have {weeks_left} weeks left.")

# Shorter version 

# age = input()
# Your code below this line 👇
# years = 90 - int(age)
# weeks_left = years * 52

# print(f"You have {weeks_left} weeks left.")
