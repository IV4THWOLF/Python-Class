##Devon Lowery
##Project 2

#Get the user's name.
name = input("Hi! What is your name?")

#Greet the user using their name and tell them the program's function.
print("Hi,", name,
      "This will tell you which rectangle has a greater area.")

#Gather data on both rectangles.
L1 = int(input("What is the length of the first rectangle?"))

W1 = int(input("What is the width of the first rectangle?"))

L2 = int(input("What is the length of the second rectangle?"))

W2 = int(input("What is the width of the second rectangle?"))

#Perform calculations.
R1 = L1 * W1

R2 = L2 * W2

#Display calculations.
print("Rectangle 1 area is", R1)
print("Rectangle 2 area is", R2)

#Display answer.
if R1 > R2:
    print(name, "Rectangle 1 has a greater area than Rectangle 2.")
else:
    print(name, "Rectangle 2 has a greater area than Rectangle 1.")

#I struggled badly with the second programming project. I think I was completing a learning curve compared to HTML.
#However, after completing the second project, I took the opportunity to build this project using the seoncd one as a base.
#Diagrams.net has made things a lot more effecient concerning creating flow charts. It's much better than doing it from scratch using Adobe Illustrator.
#In this project, I have a more firm understanding of creating a program in a general sense. As individual parts, it was easy to understand.
#Combining everything together to have a functional program with no errors was my biggest challenge between the last project and this one because I was also learning how resolve exising issues.
