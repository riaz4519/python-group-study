# some more functions
def prime(number):
    # the number should be > 1
    if(number > 1):
        
        if number in [2,3]:
            return True
        
        isPrime = True
        counter = 2;
        #   2 < 5
        #   3 < 5
        #   4 < 5
        #   5 < 5
        while(counter < number):
            # 5 % 2  = 1
            # 5 % 3 = 2
            # 5 % 4 = 1
            if(number % counter == 0):
                isPrime = False
                break
            # 2 + 1 = 3
            # 3 + 1 = 4
            # 4 + 1 = 5
            counter += 1
        return isPrime
    else:
        return False
        
print(prime(5))