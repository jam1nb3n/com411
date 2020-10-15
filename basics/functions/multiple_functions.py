def display_ladder(steps):
    i = 0
    while (i < steps):
        print("| |")
        print("|-|")
        i += 1

def create_ladder():
    display_ladder(int(input("How many steps remain?\n")))

create_ladder()