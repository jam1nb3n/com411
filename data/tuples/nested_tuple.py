def steps():
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]
    return likelihoods

def run():
    likelihoodsLocal = steps()
    good_steps = []
    bad_steps = []

    for x in likelihoodsLocal:
        if (x[1] < 50):
            good_steps.append(x)
        else:
            bad_steps.append(x)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()