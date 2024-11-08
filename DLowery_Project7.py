#Name: Devon Lowery
#Project: Functions
#Description: Using python to create a program that converts cups to tablespoons and vise versa.

#Function 1: conversion to cups
def cupsToTbsps(cupsEntered):
    total = cupsEntered * 16
    return total

#Function 2: conversion to tbsp
def tbspsToCups(tbspsEntered):
    total = tbspsEntered / 16
    return total

#Function 3: Main function
def main():
    #Begin while loop
    playAgain = "Y"
    while playAgain == "Y" or playAgain == "y":
        conversion = input("Which conversion would you like to do: tablespoons or to cups? Enter C or T")
        if conversion == "C" or conversion == "c":
            cupsEntered = float(input("Enter number of cups:"))
            print(cupsToTbsps(cupsEntered))
            playAgain = input("Would you like to play again? Y or N")
        else:
            tbspsEntered = float(input("Enter number of tbsps:"))
            print(tbspsToCups(tbspsEntered))
            playAgain = input("Would you like to play again? Y or N")
        #end if
    print("Thanks for playing!")
    #end while
main()
