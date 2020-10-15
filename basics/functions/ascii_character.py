print("Program Started!")
asciiCode = abs(int(input("Please enter an ASCII code:\n")))
if (31 < asciiCode < 126):
    print(f"The character represented by the ASCII code {asciiCode} is {chr(asciiCode)}")
else:
    print("no")
print("Program Ended!")