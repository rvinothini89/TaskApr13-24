#Program to print string without vowels
str= input("Enter string:")
#Defining list with vowels
vow = ["a","e","i","o","u"]
# using nested loop to compare string and vowel and printing without vowel
for x in str:
    for y in vow:
        if x == y:
            str = str.replace(x,"")
print("String without vowels: ",str)