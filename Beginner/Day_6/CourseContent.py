# ## Function

# print("Hello")
# num_char = len("Hello")
# print(num_char)

# ## Make our own function

# def my_function():
#   print("Hello")
#   print("Bye")

# my_function()

## IndentationError

# def test():
#   print("Hello")
#   print("Hello")

# def my_function():
#   if sky == "clear":
#     print("blue")
#   elif sky == "cloudy":
#     print("grey")
#   print("Hello")
# print("World")

## While loops

# for item in list_of_items:
#   Do something to each item

# for number in range(a, b):
#   print(number)

# while something_is_true:
#   Do something repeatedly

fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
  print(fruits) #This can't be done easily with a while loop

fruits = ["Apple", "Pear", "Orange"]
for n in range(1, 6):
  print(n)

#While loops are used when we don't care about the number of sequence we are in
#We just want to carry out some sort of functionnality many times until a condition is met

#While loops are more dangerous than for loops
#
