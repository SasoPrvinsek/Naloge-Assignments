a = [3, 3, 4, 1, 2, 4]
sestevek = 0

for element in a:
    sestevek += element
    
print(sestevek)

def vsota(s = [1, 2, 3]):
    rezultat = 0
    for element in s:
        rezultat += element

    return rezultat    
    
rez = vsota(a)
print(rez)    

rez = vsota()
print(rez)

print(sum(a))