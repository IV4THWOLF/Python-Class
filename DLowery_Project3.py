##Devon Lowery
##Project 3

#Get the user's name.
name = input("Hello! What is your name?")

#Greet the user using their name and tell them the purpose of the program.
print("Hi,",name)
print("This was created to tell you which generation you are a part of.")

#Obtain user's birth year.
year = int(input("What year were you born?"))

#Tell user their generation(s).

#Order of list:
#Silent Generation (<=1945)
#Baby Boomers (1946-1964)
#Gen X/Xennials (1975-1980)
#Gen X (1965-1980)
#Milennial/Xennials (1981-1983)
#Millennial/Zillennials (1993-1996)
#Millennial (1981-1996)
#Gen Z/Zillennials (1997 & 1998)
#Gen Z (1997-2012)
#Gen Alpha (2012-2025)

if year <=1945:
    print(name,"You are a part of The Silent Generation! You are really wise!")
elif year <1965:
        print(name,"You are a part of the Baby Boomers generation! Make sure you still have plenty of fun!")
    elif year >= 1975 and year <=1980 then:
            print(name,"You are a part of Gen X! You are also considered to be a part of the Xennials generation!")
        elif year <1981 then:
                print(name,"You are a part of Gen X! Enjoy yourself!")
            elif year >=1981 and year <=1983 then:
                    print(name,"You are a Millennial! Also, you are considered to be a part of the Xennials generation!")
                elif year >=1993 and year<=1996 then:
                        print(name,"You are a Millennial! Aslo know you are a part of the Zillennials generation!")
                    elif year <1997 then:
                            print(name,"You are a Millennials! Enjoy all of your passions")
                        elif year >=1997 and year <=1998 then:
                                print(name,"You are a part of Gen Z! You are also a part of the Zillennials generation!")
                            elif year <2013 then:
                                    print(name,"You are a part of Gen Z! Make sure you have a lot of fun!")
                                elif year <=2025 then:
                                        print(name,"You are a part of Gen Alpha! Prepare to have a lot of fun!")
#if end
                                        

