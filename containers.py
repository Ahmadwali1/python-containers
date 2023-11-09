#Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student’s name.
# Print out the last student’s name.

#Solution
# students = ['Bob', 'Ahmad', 'james', 'Alex']
# print(students[1])
# print(students[-1])

#Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string “[food goes here] is a good food”.

#Solution 
# foods = ('Burger', 'Pizza', 'Bread', 'taco')
# for food in foods:
#   print(f"{food} is a good food")

#Exercise 3
#Using a for loop, print just the last two food strings from foods.

#Solution
foods = ('Burger', 'Pizza', 'Bread', 'taco')
for food in foods[2:4]:
  print(f"{food} is a good food")