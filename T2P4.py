#Program to print string with unique characters
str = input("Enter String:")
#Here trying to get count of each character, character with more than one occurance replaced with ""
for x in str:
    if (str.count(x) > 1):
        str = str.replace(x,"")
print("String with unique characters: " +str)