def run():
    coverType = input("What type of cover does the book have?\n")
    if (coverType == "soft"):
        perfectBound = input("Is the book perfect-bound?\n")
        if (perfectBound == "yes"):
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books")
    else:
        print("Books with hard covers can be more expensive!")
