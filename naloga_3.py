import math

hitrost = float(input("vnesi hitrost (m/s): "))
kot = math.radians(float(input("vnesi kot (°): ")))
s = (hitrost**2 * math.sin(2*kot))/9.8
print("razdalja je enaka:", s)