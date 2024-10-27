#Name: Devon Lowery
#Project 4
#This project reminds me of using microsoft excel to keep track of my expenses. Overall, I like how flexible python is as a language.

#Begin Counter
counter = 1

#Start while loop
while counter <= 5:

#User enters how much was spent over the last five times eating at a restaurant
    Meal1 = int(input("How much did you spend for first meal?"))
    Meal2 = int(input("How much did you spend the second meal?"))
    Meal3 = int(input("How much did you spend the third meal?"))
    Meal4 = int(input("How much did you spend the fourth meal?"))
    Meal5 = int(input("How much did you spend the fifth meal?"))

#Calculate total
    mealsTotal = Meal1 + Meal2 + Meal3 + Meal4 + Meal5

#Calculate average
    average = mealsTotal/5
    if average <10:
        print("Your total for all five meals is $",mealsTotal, "and your average amount is $",average,"per meal. You're saving a lot of money!")
    elif average <15:
        print("Your total for all five meals is $",mealsTotal,"and your average amount is $",average,"per meal. You're doing pretty well overall.")
    elif average >=15 and average <=20:
        print("Your total for all five meals is $",mealsTotal,"and your average amount is $",average,"per meal. There's room for improvement to save money.")
    elif average >20:
        print("Your total for all five meals is $",mealsTotal,"and your average amount is $",average,"per meal. Consider budgeting for every restaurant.")
    #End if
    
    #Repeat loop if requested
    Repeat = input("Do it again? Y or N?")
    if Repeat == "Y" or Repeat == "y":
        counter += 1
        print("Okay! I'll reset everything.")
    else:
        counter += 6
        print()
   
if counter > 5:
    print("You've reached the end of this program. Have a good day!")
