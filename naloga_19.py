seznam = [6, 4, -15, 10, 5, 3, -2, 9, -8]

def absolutno(st):
    if st > 0:
        return st
    return st * -1

def najvecji(s):
    naj = None
    
    for element in s:
        if naj == None:
            naj = element
        if absolutno(naj) < absolutno(element):
            naj = element
    
    return naj

print(najvecji(seznam))

