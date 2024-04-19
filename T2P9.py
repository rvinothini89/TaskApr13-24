#Program to find number of words in a string
#Getting string as input
str1 = input("Enter string:")
#Splitting the string using space and storing in the list variable
mylist = (str1.split(" "))
#printing list output to make sure if its split correctly
print(mylist)
wCount = len(mylist)
print("Number of words in provided string is " , wCount)