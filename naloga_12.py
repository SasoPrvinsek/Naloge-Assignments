rezOne = 0
rezTwo = 0

while rezOne - rezTwo < 2 and rezTwo - rezOne < 2: #je enako kot abs(rezOne - rezTwo) < 2 
    stOne = int(input("tekmovalec 1 izbere stevilo: "))
    stTwo = int(input("tekmovalec 1 izbere stevilo: "))
    rez = int(input("tekmovalec 2 napise rezultat: "))
    
    if rez == stOne * stTwo:
        rezTwo += 1
    print("\n")

    stOne = int(input("tekmovalec 2 izbere stevilo: "))
    stTwo = int(input("tekmovalec 2 izbere stevilo: "))
    rez = int(input("tekmovalec 1 napise rezultat: "))

    if rez == stOne * stTwo:
        rezOne += 1
    print("\n")    

    print("trenutni rezultat = ", rezOne, ":", rezTwo)            
    print("\n")


