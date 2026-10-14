# Q1 - Write a Program to read a File and count how many vowels are present in its content
with open("myFile.txt","r") as f:
    content = f.read()
# print(content)
vowel = 0
for ch in content.lower():
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        vowel = vowel + 1
print("Count of Vowels: ",vowel)