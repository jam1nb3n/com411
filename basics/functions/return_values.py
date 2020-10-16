def sum_weights(beep, bop):
    return (beep+bop)

def calc_avg_weight (beep, bop):
    return ((sum_weights(beep, bop))/2)

def run():
    beep = int(input("Beep: "))
    bop = int(input("Bop: "))
    runMode = input("What would you like to calculate (sum or average)?\n")
    if (runMode == "sum"):
        print(sum_weights(beep, bop))
    if (runMode == "average"):
        print(calc_avg_weight(beep, bop))