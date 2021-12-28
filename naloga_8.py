skupna = 0
cena = float(input("cena izdelka: "))

while cena != 0:
    skupna = skupna + cena
    cena = float(input("cena izdelka: "))

print(skupna)