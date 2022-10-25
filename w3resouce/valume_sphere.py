# v  variable
#v = 4/3 (pi*r3)
from math import pi, pow

r = float(input("insert radius : "))
v = 4/3 * (pi*pow(r, 3))
print("%.2f"%(v))
