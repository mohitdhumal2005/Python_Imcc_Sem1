text = "   Mastaa ree !! Euu   "

#Removing Spaces from front as well as from End-- strip()
print("Remove Spaces:",text.strip())

text = text.strip() #Removing Spaces from front as well as from End--

# LowerCase: lower()
print("LowerCase:",text.lower())

#UpperCase: upper()
print("UpperCase:",text.upper())

#Capitalize: Pahilya Letter Capital Hoto from akkha sentence
print("Capitalize: ",text.capitalize())

#title() - Makes Every First letter capital
print(text.title())

#count() - counts the occurences
print("Letter E occurs",text.count('e'),"times in the text")

#find() - returns the index 
print("Position of Substring ree in text is: ",text.find("ree"))

# replace() - replaces the string
print(text.replace("Mastaa","Hello"))

# startswith() - Returns True if it starts with the desired string
print(text.startswith("Mastaa"))

#  endswith() - Returns True if if ends with correct string
print(text.endswith("hi"))

# split() - it splits the words into a List
print("Simple Split: ",text.split())

# join() - joins the list into single sentence
wordss = ["My","name","is","Mohit"]
print(" ".join(wordss))