from random import randint

a = randint(4,12)
b = randint(4,12)

rez = a*b
rezultat = int(input("koliko je " + str(a) + " * " + str(b) + "? "))

if rez == rezultat:
    print("pravilno")
else:
    print("napacno")