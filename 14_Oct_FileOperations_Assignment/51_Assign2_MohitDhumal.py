# Q2 -Read all lines from a file into list. Print the total No. of lines and display the 2nd and 4th line.
with open("myFile.txt","r") as f:
    lines = f.readlines()
# print(lines)

total_Lines = len(lines)
print("Total No. of Lines: ",total_Lines)
print("2nd Line from the file: ",lines[1],end="")
print("4th Line from the file: ",lines[3])
