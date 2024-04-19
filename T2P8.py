#Program to find if the strings are anagram of each other
str = input("Enter first string:")
str1 = input ("Enter second string:")
#using sorted function to check if the sorted output match the other string
if sorted(str) == sorted(str1):
    print("True String is anagram of another")
else:
    print("False String is not anagram of another")