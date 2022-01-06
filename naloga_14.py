stevilo = int(input("izberi stevilo: "))
seznam = []

while stevilo / 10 != 0:
    seznam.append(stevilo % 10)
    #print(seznam)
    stevilo = int(stevilo / 10)
    #print(stevilo)
    #print("--------")
    
novoStevilo = 0

for element in seznam:
    novoStevilo *= 10
    #print(novoStevilo)
    novoStevilo += element
    #print(novoStevilo)
    #print("--------")

print(novoStevilo)
