# n = 11
# r = n + 1

# for i in range(1,n):# 2
#     for s in range(1,i):
#         print(" ",end="")
#     for j in range(1,r-i):
#        print ("*",end=" ")
#     print ()
n = 11
for i in range(1,n):
    for s in range(1,n-i):
        print (" ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print ()
    
    
