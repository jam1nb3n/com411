print("Program Started!")
inputString = input("Please enter a standard character:\n")

if (len(inputString) == 1):
    print(f"The Ascii code for {inputString} is: {ord(inputString)}")
else:
    print("invalid character entered")
print("Program Ended!")