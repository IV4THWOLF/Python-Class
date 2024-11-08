#Name: Devon Lowery
#Project 8: Validation
#Description: Creating a calculator to determine an employee's gross pay.

#Rules:
#Range of pay: $7.50 - 18.25 (1st)
#Range of hours: 0 - 40 (2nd)
#Displaying gross pay (last)

payRate = float(input("Enter pay rate (7.50 to 18.25):"))
while payRate < 7.50 or payRate > 18.25:
    print("Error: Please enter a number between 7.50 and 18.25")
    payRate = float(input("Enter pay rate:"))  
print("The pay rate you've entered is ",payRate)

hoursWorked = float(input("Enter hours worked (0 to 40): "))
while hoursWorked < 0 or hoursWorked > 40:
    print("Error: Please enter a number between 0 and 40")
    hoursWorked = float(input("Enter hours worked: "))
print("The hours work you've entered is",hoursWorked)

grossPay = payRate * hoursWorked
print("Based on what you've entered, your gross pay is $",grossPay)

#Reflection: Having the opportunity to watch some of Bro Code's videos, this project was very easy. He discussed validations in while loop video.
#For me, this project help exercise basic concepts I've developed in previous projects. A change I have made since my last coding project is making
#making things more color coordinated and changing IDLE to a dark profile. Having a keen eye for details, colors helps me tell the difference
#between different parts of my code. I am more confident in my skills using python as time progresses and I am seeing my progress.
