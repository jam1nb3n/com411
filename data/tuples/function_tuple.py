def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    minMax = (min(likelihoods), max(likelihoods))
    return minMax

def run():
    print(f"Minimum likelihood of falling: {likelihood()[0]}%")
    print(f"Maximum likelihood of falling: {likelihood()[1]}%")

run()