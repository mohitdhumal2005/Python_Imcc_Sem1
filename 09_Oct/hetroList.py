# # Create a heterogenous list of numbers and names. Split the list from highest number
# a = "hello mohit how are you"
# b = a.split()
# print(b)
# c = " ".join(b)
# print(c)

list1 = [1,"Ajay",2,131,19,3,5,"Seema","Anita","Mohit"]  #O/p = [1,"Ajay",2,3][5,"Seema","Anita"]
nums = []

for i in list1:
    if type(i)==int:
        nums.append(i)
print(nums)

maxNum = max(nums)
print("Maximum no. is: ",maxNum)
indexOfMaxNum = list1.index(maxNum)
print("Index of MaxNum in Og List: ",indexOfMaxNum)


print(list1[:indexOfMaxNum])
print(list1[indexOfMaxNum:])


