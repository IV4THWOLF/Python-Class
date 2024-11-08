#Name: Devon Lowery
#Project Name: "RNGesus"
#Description: Using a random number generator to understand how perks are generated in the game Destiny 2.

#Note:"RNGesus" (a joke) is an idea of an electronic figure in power that allows players to obtain what they're looking for. Within the Destiny 2 community,
#some players obtain the weapons with perks they want quickly, while other players may have to repeat an activity numerous times before getting the same.

import random

#First Column: Barrel perks
def columnOne():
    barrel = random.randint(1, 9)
    1 == "Arrowhead Brake",
    2 == "Chambered Compensator",
    3 == "Corkscrew Rifling",
    4 == "Extended Barrel",
    5 == "Fluted Barrel",
    6 == "Full Bore",
    7 == "Hammerforged Rifling",
    8 == "Polygonal Rifling",
    9 == "Smallbore"
    print(len(barrel))
    return barrel
#end function

#Second Column: Magazine perks
def columnTwo():
    mag = random.randint(1, 7)
    1 == "Accurized Rounds"
    2 == "Appended Mag"
    3 == "Tactical Mag"
    4 == "Extended Mag"
    5 == "Steady Rounds"
    6 == "Alloy Magazine"
    7 == "Flared Magwell"
    print(mag)
    return mag
#end module

#Third Column: First set of interactive perks
def columnThree():
    interactOne = random.randint(1, 7)
    1 == "Rapid Hit"
    2 == "Demolitionist"
    3 == "Destablizing Rounds"
    4 == "Air Trigger"
    5 == "Eye of the Storm"
    6 == "Lone Wolf"
    7 == "Rampage"
    print(interactOne)
    return interactOne
#end module

#Fourth Column: Second set of interactive perks
def columnFour():
    interactTwo = random.randint(1, 7)
    1 == "Harmony"
    2 == "Swashbuckler"
    3 == "To the Pain"
    4 == "Closing Time"
    5 == "Rangefinder"
    6 == "Explosive Rounds"
    7 == "Kill Clip"
    print(interactTwo)
    return interactTwo
#end module
    
gunName = "Ancient_Gospel"
print(gunName)

def gun():
    columnOne()
    columnTwo()
    columnThree()
    columnFour()
gun()
