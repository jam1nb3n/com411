adventureType = input("What type of adventure should I have?\n")

if ((adventureType == "short") or (adventureType == "scary")):
    print("Entering the dark forest!")

elif ((adventureType == "safe") or (adventureType == "long")):
    print("Taking the safe route!")

else:
    print("Not sure which route to take.")