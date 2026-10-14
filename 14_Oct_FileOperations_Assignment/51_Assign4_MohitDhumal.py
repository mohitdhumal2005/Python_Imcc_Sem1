# Read a file, split its content into words, and store them into list 
    # i. Print the Total No. of Words
    #  ii. Print all unique words   
with open("myFile.txt", "r") as file:
    content = file.read()
words = content.split()
print("Total number of words:", len(words))

unique_words = []

for ch in words:
    if ch not in unique_words:
        unique_words.append(ch)
print("Unique words:", unique_words)   