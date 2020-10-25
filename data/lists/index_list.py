def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    movement = movements()
    movementLen = len(movement)
    i = 0
    while(i < movementLen):
        print(f"{movement[i]} for {movement[i+1]} steps")
        i += 2

run()