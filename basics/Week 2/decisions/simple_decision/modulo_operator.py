inputNumber = int(input("Please enter a whole number: "))
if((inputNumber % 2) == 0):
    isEven = "even"
else:
    isEven = "odd"
print(f"The number {inputNumber} is {isEven}")