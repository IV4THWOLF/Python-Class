#Name: Devon Lowery
#Project 6: Modules
#Description: Calculating proper tax amounts for both the county and state.

#Explanation for use of modules: For this project, I'll be using separating each module by grouping together the general purpose to help keep structure.
#By organizing different parts of the program, it will allow me to easily find the section of code to edit when neceesary as well as troubleshoot any issues quicker.

#Variable: Define tax rates
County_Tax_Rate = .02
State_Tax_Rate = .04

#Gather data
totalSales = float(input("Enter total sales for the month: $"))

#First Module: Total Sales (Shows total)
def Total_Sales():
    print("Your total is $",totalSales)
#end module

#Second Module: Local Taxes (Calculates county taxes. Can change county to city if necessary in the future)
def Local_Tax():
    countyTax = totalSales * County_Tax_Rate
    print("The local tax is $",countyTax)
#end module

#Third Module: State Taxes (Calculates state taxes.)
def State_Tax():
    stateTax = totalSales * State_Tax_Rate
    print("The state tax is $",stateTax)
#end module

#Fourth Module: Total Calculation (Shows totals.)
def Total_Taxes():
    countyTax = totalSales * County_Tax_Rate
    stateTax = totalSales * State_Tax_Rate
    Total_Tax = countyTax + stateTax
    print("Total taxes is $",Total_Tax)
#end module

#Fifth Module: Showing Results (Displays results.)
Total_Sales()
Local_Tax()
State_Tax()
Total_Taxes()
#end module

#Reflection: Once I fully understood how everything worked with each other, I wasn't as frustrated trying to understand the code nor troubleshoot my issues. Not knowing for
#a period of time that everything inside a module will not be recognized outside of the module was extremely frustrating. I think because I'm so used to everything working in
#conjunction with one another that having something different was a slight learning curve. As of now, I can't see myself using this function in the future. Maybe if I find a
#way to use it outside of something similar to a calculator, I'll see the bigger picture and how it can be really effective.
