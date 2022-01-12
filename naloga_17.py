bes = "ta suhi skafec pusca"

"""
def steviloA(beseda):
    stA = 0
    for element in beseda:
        if element == "a":
            stA += 1
    return stA

print(steviloA(bes))"""

def steviloZ(beseda, znak):
    stZ = 0
    for element in beseda:
        if element == znak:
            stZ += 1
    return stZ

print(steviloZ(bes, "s"))

def steviloA(beseda):
    return steviloZ(beseda, "a")

print(steviloA(bes))