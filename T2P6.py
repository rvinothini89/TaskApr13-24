#program to find common sub string from provided two strings
str = input("Enter first string:")
str1 = input ("Enter second string:")
answer = ""
len1 = len(str)
len2 = len(str1)
for i in range(len1):
    for j in range(len2):
        temp = 0
        match = ''
        while ((i+temp < len1) and (j+temp<len2) and str[i+temp] == str1[j+temp]):
                match += str1[j+temp]
                temp += 1
        if len(match) > len(answer):
                answer = match
print(answer)