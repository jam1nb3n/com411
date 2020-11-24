import random as rnd
import matplotlib.pyplot as plt

def data():
    paths = {}
    paths["lineType"] = input("Enter line type (--/-): ")
    paths["lineColour"] = input("Enter line colour (r/g/b): ")
    paths["markerStyle"] = input("enter marker style (o/s/^): ")
    return paths

def generate():
    numberOfLines = int(input("How many lines would you like to display?: "))
    i = 0
    while (i < numberOfLines):
        values = data()
        x = rnd.sample(range(-5,5), 5)
        y = rnd.sample(range(-5,5), 5)
        args = f"{values['lineType']}{values['lineColour']}{values['markerStyle']}"
        plt.plot(x, y, args)
        i += 1
    plt.show()

def run():
    print("Running")
    generate()
    print("Done!")