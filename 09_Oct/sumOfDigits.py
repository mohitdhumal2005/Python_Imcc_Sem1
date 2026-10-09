n = int(input("Enter a Number: "))
sum = 0
while(n>0):
    mod = n%10
    sum = sum + mod
    n=n//10
print("Sum of Digits is: ",sum)