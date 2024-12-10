#Name: Devon Lowery
#Project 9: Arrays
#Description: Producing an array of people names and ages.

#Requirements:
#1. a String array named people that is initialized with the names of five people
#2. a String array named age is initialized with their ages
#3. Print the 2D array.

#Define variable data
people = ["Sofia", "Sage", "Rouge", "Filo", "Cleopatra"]
age = [10, 8, 6, 4, 2]
#Display 2D array data
rows = 2
columns = 5
peopleAges = [ ["Sofia", "Sage", "Rouge", "Filo", "Cleopatra"],
                       [10, 8, 6, 4, 2]
]
#Print 2D array
print("Name:",peopleAges[0][0],", Age:",peopleAges[1][0])
print("Name:",peopleAges[0][1],", Age:",peopleAges[1][1])
print("Name:",peopleAges[0][2],", Age:",peopleAges[1][2])
print("Name:",peopleAges[0][3],", Age:",peopleAges[1][3])
print("Name:",peopleAges[0][4],", Age:",peopleAges[1][4])



#Reflection: With a personal project I'm conducting using the random number command, this will help try to resolve a challege
#that I'm currently facing. My goal is to recreate the same program used in a video game along the lines of a random number generator.
#The challege I currently face is trying to get the program to display strings instead of integers. Perhaps these arrays will help add a
#piece to the puzzle in showing those strings. I think I like using the list more than arrays as it's tedious to continously type every point
#in the table instead of having a way to automate it.
