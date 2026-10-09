n = int(input("Enter a Number: "))
sum = 0
if n<=0:
    print("Number Should not be Negative or O")
else:
    while(n>0):
        mod = n%10
        sum = sum + mod
        n=n//10
    print("Sum of Digits is: ",sum)