# Write your code here 👇
target = 100
total = 0
for number in range (0, target):
  total = number + 1
  if total % 3 == 0 and total % 5 == 0:
    print("FizzBuzz")
  elif total % 3 == 0:
    print("Fizz")
  elif total % 5 == 0:
    print("Buzz")
  else:
    print(total)

#Angela Version

target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
