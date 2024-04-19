# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
#print(student_heights[n]) #affiche le dernier item de la liste

total_height = 0
num_students = 0
average_height = 0

for height in student_heights:
  total_height += height

for student in student_heights:
  num_students += 1

average_height = total_height / num_students
average_height = round(average_height)

print(f"total height = {total_height}")
print(f"number of students = {num_students}")
print(f"average height = {average_height}")

#Angela version

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")
