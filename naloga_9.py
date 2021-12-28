skupna = 0
izdelkov = 0
cena = float(input("cena izdelka: "))

while cena != 0:
    skupna = skupna + cena
    izdelkov += 1
    cena = float(input("cena izdelka: "))

print(skupna)
print(skupna/izdelkov)
