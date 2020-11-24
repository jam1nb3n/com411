import matplotlib.pyplot as plt

def coordinate():
    x = int(input("Please enter an X value: "))
    y = int(input("Please enter a Y value: "))
    return (x,y)

def path():
    print("Retriving Path...")
    x_values = []
    y_values = []
    i = 0
    while (i < 4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])
        i += 1
    return [x_values, y_values]

def run():
    values = path()
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.plot(values[0],values[1],"ro--")
    plt.show()

run()