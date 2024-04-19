#Program to total number of vowels and count of each vowel in given string
str = "Guvi Geeks Network Private Limited"
vow = ["a","e","i","o","u"]
ctr = 0
for x in str:
    for y in vow:
        if x==y:
            ctr = ctr+1
print("Total number of vowels present in given string is",ctr)
#using list and dictionary comprehension to check if the char matching the vowel
count = {x:sum([1 for char in str if char == x]) for x in 'aeiou'}
print("Number of each vowel in given string is: ",count)