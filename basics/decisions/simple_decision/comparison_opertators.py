def run():
    numOne = int(input("Please enter the first number: "))
    numTwo = int(input("Please enter the second number: "))

    if (numOne > numTwo):
        print(f"{numOne} is largest")
    else:
        print(f"{numTwo} is largest")