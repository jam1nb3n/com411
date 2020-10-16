def run():
    paintDiriction = input("Towards which direction should I paint (up, down, left or right)?\n")
    if (paintDiriction == "up"):
        print("I am painting in the upward direction!")
    elif (paintDiriction == "down"):
        print("I am painting in the downward direction!")
    elif (paintDiriction == "left"):
        print("I am painting in the leftward direction!")
    elif (paintDiriction == "right"):
        print("I am painting in the rightward direction!")
    else:
        print("Unknown direction")