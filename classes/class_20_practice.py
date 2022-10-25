# """ 2 - 1
#     N   l   sub 
#     7 - o * 2 = 0
#     5 - 1 * 2 = 2
#     3 - 2 * 2 = 4
#     1 - 3 * 2 = 6

#line
# 9 / 2 = 4.5 = 5
# 7 / 2 = 3.5 = 4

# *******
#  *****
#   ***
#    *
# """
from math import ceil
n = 7
line = ceil(n / 2)

for i in range(0,line):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,n-(i*2)):
        print("*",end="")
    print()
    
    