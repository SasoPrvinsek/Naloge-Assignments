import random

def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "-":
        return a - b
    else:  
        return a / b
    
x = random.randint(5, 15)
y = random.randint(1, 10)

print(calc(x, y, "-"))
print(calc(y, x, "+"))

