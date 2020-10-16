def run():
    name = input("Name? ")
    age = int(input("Age in years? "))
    height = float(input("Height in metres? "))
    weight = float(input("Weight in Kg? "))

    print("Name: ", name)
    print("Age:", str(age))
    print("Height: ", str(round(height, 2)))
    print("Weight: ", str(round(weight, 2)))
    BMI = weight / (height ** 2)
    print("BMI: ", round(BMI, 2))
