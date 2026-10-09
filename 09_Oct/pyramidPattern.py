# n = int(input("Enter a number: "))
# for i in range(n+1):
#     print(" " * (n-i) + "*" * (2*i-1))
    
    
    
n = int(input("Enter a Number: "))
for i in range(n):
    print(" "*(n-i),end="")
    for j in range((2*i)+1):
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
    
    print()