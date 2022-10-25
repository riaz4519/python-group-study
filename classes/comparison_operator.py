# >
# number1 = 10
# number2 = 10

# compare = number2 > number1

# if(number2 > number1):
#     print("number two is greater than number 1")
    
# elif(number2 < number1):
#     print("number 2 is less then number 1")
    
# elif (number2 == number1):
#     print("number 2 is equal to number 1")
# else:
#     print("number 2 is not greater than number one")

# print(compare,type(compare))



# <
# ==
# !=
# >= greater than equal
# <= less than equal
# is
# is not

#A+ = 80 - 100
#A  = 70 - 79
#A- = 60 - 69

#Md. Hasan Mahmud Shanto
# grading system
# num1=float(input ("enter the mark: "))

# if( num1 >= 80 ):
#     if(num1>=80 and num1<=100):
#         print("he got A+")
#     else:
#         print("number out of bounds")
    
# elif(num1 >= 70 ):
#     print("he got A")   
# elif(num1>=60 ):
#     print("he got B") 
# elif(num1>=50 ) :
#     print("he got C") 
# elif(num1<=40 ) :
#     print("he failed") 
# else :
#     print("number out of range")

# marks = 65
# for marks in range (80,100):
#     print("you get A+")

# for marks in range (70,80):
#     print("you get A")
# for marks in range (60,70):
#     print("you get A-")
# for marks in range (50,60):
#     print("you get B+")
# for marks in range (40,50):
#     print("you get B")


# range_values = list(range(80,100))
# print(range_values)

mark = float(input("Enter your mark to get Grade : "))

#pass D
if(mark <= 39 and mark >= 0):
    print("you get F");
elif(mark >= 40 and mark <= 49):
    print("you get D");
elif (mark >= 50 and mark <= 59 ):
    print("you get C")
elif (mark >= 60 and mark <= 69 ):
    print("you get B")
elif (mark >= 70 and mark <= 79 ):
    print("you get A")
elif (mark >= 80 and mark <= 100 ):
    print("you get A")
else :
    print("Invalid input for a grade")
    
    
    


