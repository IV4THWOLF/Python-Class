#Name: Devon Lowery
#Project 10: Files
#Description: Creating, opening, modifying, reading, closing, and deleting a file.

#Import library
import os

#Create and open file. File name: names.txt. Create through write function.
def writeFile():
    names_file = open("names.txt", "w")
    #Input names and close file.
    names_file.write("Olivia Johnson\n")
    names_file.write("Ethan Williams\n")
    names_file.write("Sophia Martinez\n")
    names_file.write("Mason Lee\n")
    names_file.write("Isabella Garcia\n")
    names_file.close()

#Create read function
def readFile():
    infile = open("names.txt", "r")
    #Read and count names.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    #Remove "\n"
    line1 = line1.rstrip("\n")
    line2 = line2.rstrip("\n")
    line3 = line3.rstrip("\n")
    line4 = line4.rstrip("\n")
    line5 = line5.rstrip("\n")
    #Close file.
    infile.close()
    #Return lines so they can be read in the print function
    return line1, line2, line3, line4, line5

#Create print function
def printFile():
    #Retrieve names from readFile function
    line1, line2, line3, line4, line5 = readFile()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

#Create main function
def main():
    #Call previous three functions
    writeFile()
    readFile()
    printFile()

#Call main function
main()

#Delete file.
def deleteFile():
    os.remove("names.txt")
    print("The name file has been deleted successfully")

deleteFile()

#Reflection:
#I enjoyed writing this program. It's good to be able to use what I've learned to make a well structured program. I've known that python can be used
#to create a multitude of programs. I've been slowly trying to figure out how and what code could be used to impact what functions within a device.
#I never thought about creating text documents using python but that's because I'm so used to using the GUI to quickly achieve that goal. As for resources,
#I've downloaded Microsoft's Visual Studio Code due to Visual Studio no longer being supported on Mac's. It helps with debugging and pointing out
#problems, which is a really neat feature to have when sometimes forgetting things that will cause errors in a program.