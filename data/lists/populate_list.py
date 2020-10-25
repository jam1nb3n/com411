import iterate_list

def directions():
    return iterate_list.directions()

def menu():
    iterate_list.menu()
    directionsLocal = directions()
    return directionsLocal[(int(input("\n")))]
    
def run():
    route = []
    print("Working out escape route...\n")
    i = 0
    while (i < 5):
        route.append(menu())
        i += 1
    print("Escape Route: " + route)

run()