def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction")
    directionsLocal = directions()
    i = 0
    while (i < len(directionsLocal)):
        print(f"{i}: {directionsLocal[i]}")
        i += 1
    
def run():
    menu()

run()