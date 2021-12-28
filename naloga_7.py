izdelkov = int(input("koliko je izdelkov na blagajni? "))
skupna = 0
for _ in range(izdelkov):
    cena = float(input("cena izdelka: "))
    skupna = skupna + cena
 
print(skupna)
