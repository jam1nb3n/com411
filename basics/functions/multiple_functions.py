def display_ladder(steps):
    i = 0
    while (i < steps):
        print("| |")
        print("|-|")
        i += 1

def run():
    display_ladder(int(input("How many steps remain?\n")))
