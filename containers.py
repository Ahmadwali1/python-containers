#Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student’s name.
# Print out the last student’s name.

#Solution
students = ['Bob', 'Ahmad', 'james', 'Alex']
# print(students[1])
# print(students[-1])

#Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string “[food goes here] is a good food”.

#Solution 
foods = ('Burger', 'Pizza', 'Bread', 'taco')
# for food in foods:
#   print(f"{food} is a good food")

#Exercise 3
#Using a for loop, print just the last two food strings from foods.

#Solution
# foods = ('Burger', 'Pizza', 'Bread', 'taco')
# for food in foods[2:4]:
#   print(f"{food} is a good food")

#Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# “I was born in city, state - population of population”

#Solution
# home_town = {
#   'city': 'Houston',
#   'state': 'Texas',
#   'population': '29.53 million' 
# }
# print(f"I was born in {home_town['city']}, {home_town['state']}-{home_town['population']}")

#exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# “city = Arcadia”
# “state = California”
# “population = 58000”

#solution
# for key, value in home_town.items():
#   print(f"{key} = {value}")

#exercise 6
# Create an empty list named cohort.
# Using a for loop to iterate over the students list.
# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student’s name and the food in the foods list at the same index

#solution
cohort = []
for idx, student in enumerate(students):
  student_data = {
    'name': student,
    'fav_food': foods[idx]
  }
  cohort.append(student_data)
print(cohort)

