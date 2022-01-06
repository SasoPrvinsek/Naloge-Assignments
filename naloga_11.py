import random

def vrzi():
    return random.choice("GC")

stKov = 5

while stKov != 0 and stKov != 10:
    kovanc = vrzi()
    if vrzi() == "G":
        stKov -= 1
    else:
        stKov += 1
    print(kovanc, stKov)

