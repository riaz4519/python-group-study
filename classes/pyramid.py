#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6



n = 7
for i in range(1,n):
    for s in range(1,n-i):#5
        print(" ",end="")
    for j in range(1,i + 1):
        print(j,end=" ") 
    print()
    
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#1 2 3 4 5 6


#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6

#1 2 3 4 5 6
#1 2 3 4 5
#1 2 3 4
#1 2 3
#1 2
#1


#1 2 3 4 5 6
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#    1 2
#     1
    