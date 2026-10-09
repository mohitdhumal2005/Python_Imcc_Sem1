name  = input("Enter name: ")
if name == name[::-1]:
    print(name,"is Palindrome")
else:
    print(name,"is not Palindrome")