stevilo = int(input("vnesi stevilo: "))
zaporedje = [stevilo]

while stevilo != 1:
    #print(int(stevilo))
    if stevilo %2 == 0:
        stevilo /= 2
    else:
        stevilo *= 3
        stevilo += 1
    zaporedje.append(int(stevilo))

#print(int(stevilo))
izpis = ""
for i, stevilo in enumerate(zaporedje):
    izpis += str(stevilo)
    if i != len(zaporedje) - 1:
        izpis += ", "

print(izpis)
