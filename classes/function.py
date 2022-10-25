# def print_my_full_name(firstname,lastname):
    
#     print(firstname + " " +lastname)
    
# def greet(name):
#     print("hello "+ name+" welcome to the group")
    
# def sum (num1,num2):
#     sum =  num1 + num2
#     return sum

# answer = sum(1,2) - 1
# print(answer)

def formated_result(number1,number2,action,result):
    
    print(number1,action,number2,"=",result)


num1 = float(input("Enter number 1 : "))
num2 = float(input("Enter number 2 : "))

operator = input("Enter a action + , - , / , * : ")

if(operator == "+"):
    sum = num1 + num2
    formated_result( number2 = num2,action= operator,result=sum,number1 = num1)
    
elif(operator == "-"):
    sub = num1 - num2
    formated_result(num1,num2,operator,sub)
    
elif(operator == "*"):
    multi = num1 * num2
    formated_result(num1,num2,operator,multi)
    
elif(operator == "/"):
    divi = num1 * num2
    formated_result(num1,num2,operator,divi)
else:
    print("invalid  operator")