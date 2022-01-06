def vprasajPrvi():
    stOne = int(input("tekmovalec 1 izbere stevilo: "))
    stTwo = int(input("tekmovalec 1 izbere stevilo: "))
    rez = int(input("tekmovalec 2 napise rezultat: "))
    print("\n")

    if rez == stOne * stTwo:
        return 1
    return 0    

def vprasajDrugi():
    stOne = int(input("tekmovalec 2 izbere stevilo: "))
    stTwo = int(input("tekmovalec 2 izbere stevilo: "))
    rez = int(input("tekmovalec 1 napise rezultat: "))
    print("\n")

    if rez == stOne * stTwo:
        return 1
    return 0    

rezOne = 0
rezTwo = 0

while rezOne - rezTwo < 2 and rezTwo - rezOne < 2: #je enako kot abs(rezOne - rezTwo) < 2 
    rezTwo += vprasajPrvi()
    rezOne += vprasajDrugi()  

    print("trenutni rezultat = ", rezOne, ":", rezTwo, "\n")     

