s = input("Enter your name: ")
print(s)
l = len(s)
print("Length of String is: ",l)

d = l//2
print("Half is: ",d)
first_half = s[:d]
second_half = s[d:]
print("First Half is: ",first_half)
print("Second Half is: ",second_half)

# Slicing
# len() function which gives length