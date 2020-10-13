lookLocation = input("Where should I look?\n")

if (lookLocation == "in the bedroom"):
    lookLocationBed = input("Where in the bedroom should I look?\n")
    if (lookLocationBed == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif (lookLocation == "in the bathroom"):
    lookLocationBath = input("Where in the bathroom should I look?\n")
    if (lookLocationBath == "in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif (lookLocation == "in the lab"):
    lookLocationLab = input("Where in the lab should I look?")
    if (lookLocationLab == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")

