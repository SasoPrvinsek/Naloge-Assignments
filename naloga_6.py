"""skupna = 0
for izdelek in range(5):
    cena = float(input("cena izdelka: "))
    skupna = skupna + cena
 
print(skupna)


ali"""

print(sum([float(input("cena izdelka: ")) for izdelek in range(5)]))