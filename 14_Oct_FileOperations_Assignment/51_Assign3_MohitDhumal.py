# Q3 - Take a sentence from user, split it into words, and store them in list. Print the longest word.

sentence = input("Enter a Sentence: ")
words = sentence.split()
# print(words)

long = words[0]

for ch in words:
    if len(ch) > len(long):
        long = ch
print("Words list:",words)
print("Longest Word:",long)