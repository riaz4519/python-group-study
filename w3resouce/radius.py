from math import pi, pow
# need radius
radius = float(input("insert radius : "))
area = pi * pow(radius, 2)

print("area of a circle is :", str(area))
print("area of a circle is : {:.2f}".format(area))
print("area of a circle is : %.2f" % (area))
