import matplotlib.pyplot as plt

def read_data(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(int(line.strip()))
    return data

def run():
    data = read_data("temps.txt")
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()

run()