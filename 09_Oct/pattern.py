#    #
#    * *
#    # # #
#    * * * *


n = int(input("Enter a Number: "))
for i in range(n):
    for j in range(i):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
    
    print()