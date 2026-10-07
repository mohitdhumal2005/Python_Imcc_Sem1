s = input("Enter a String: ").lower()
count = 0
for ch in s:
    if ch in "aeiou":
        count = count + 1

print("No. of Vowels:",count)
