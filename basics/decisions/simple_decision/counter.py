evenC = 0
numOne = int(input("Number 1: "))
if ((numOne % 2) == 0):
    evenC = evenC + 1
numTwo = int(input("Number 2: "))
if ((numTwo % 2) == 0):
    evenC = evenC + 1
numThree = int(input("Number 3: "))
if ((numThree % 2) == 0):
    evenC = evenC + 1

print(f"Odd: {str(3-evenC)}")
print(f"Even: {str(evenC)}")