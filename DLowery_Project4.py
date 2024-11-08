#Name: Devon Lowery
#Project 4
#This project reminds me of using microsoft excel to keep track of my expenses. Overall, I like how flexible python is as a language.

#Begin Counter
counter = 0
meal = 0
mealsTotal = 0

#Start while loop
while counter <= 4:

#User enters how much was spent over the last five times eating at a restaurant
    meal = int(input("How much did you spend for a meal?"))
    counter += 1
    print(meal)

#Calculate total
    mealsTotal = mealsTotal + meal

###Calculate average
    average = mealsTotal/5
    if average <10:
        print("Your total is $",mealsTotal, "and your average amount is $",average,"per meal. You're saving a lot of money!")
    elif average <15:
        print("Your total is $",mealsTotal,"and your average amount is $",average,"per meal. You're doing pretty well overall.")
    elif average >=15 and average <=20:
        print("Your total is $",mealsTotal,"and your average amount is $",average,"per meal. There's room for improvement to save money.")
    elif average >20:
        print("Your total is $",mealsTotal,"and your average amount is $",average,"per meal. Consider budgeting for every restaurant.")
    #End if
