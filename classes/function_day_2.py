#what is function 

#structure of a function parameter optional
# def name_of_the_function():
#     print("hey i have decleared a function ")

# print("welcome shanto")
# print("welcome zaed")
# print("welcome shahadat")    

# def welcome(name) : 
#     print("welcome",name)
    
# welcome("zaed")
# welcome("shant")
# welcome("shahadat")
# welcome("zaed")
    
def multi_param_welcome(first_name = "",middle_name = "",last_name = ""):
    
    if(len(first_name) > 0 or len(middle_name) > 0 or len(last_name) > 0):
        print("welcome",end=" ")
        if(len(first_name) > 0):
            print(first_name,end=" ")
        if(len(middle_name) > 0):
            print(middle_name,end=" ")
        if (len(last_name) > 0):
            print(last_name)

multi_param_welcome(first_name = "hasan",last_name ="shanto")
multi_param_welcome("hasan","","shanto")
multi_param_welcome()
