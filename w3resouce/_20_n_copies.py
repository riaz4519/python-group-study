name,n = input("Enter your name followed number of copies : ").split()

n = int(n)
if(n > 0):
    copies = (name + " ") * n
    print(copies)


