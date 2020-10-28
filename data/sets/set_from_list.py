def observed():
    inputList = []
    i = 0
    while(i < 7):
        inputList.append(input(f"Observation {i+1}: "))
        i += 1
    return inputList

def run():
    print("Counting observations...")
    inputList = observed()
    
    outputSet = set()
    for observation in inputList:
        data = (observation, inputList.count(observation))
        outputSet.add(data)
    
    for observation in outputSet:
        print(f"{observation[0]} observed {observation[1]} times")

run()