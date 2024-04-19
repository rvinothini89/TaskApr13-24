#Program to find provided string is palindrome or not
str = input("Enter your string:")
#storing reverse of original string in another string
str1 = reversed(str)
#if string and reversed string matches, its palindrome
if list(str) == list(str1):
    print("True " + "String is a palindrome")
else:
    print("False " + "String is not a palindrome")