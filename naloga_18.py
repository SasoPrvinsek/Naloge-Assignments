seznam = [6, 4, 10, 5, 3]

def najvecji(s):
    naj = None
    
    for element in s:
        if naj == None:
            naj = element
        if naj < element:
            naj = element
    
    return naj

print(najvecji(seznam))