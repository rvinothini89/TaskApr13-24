#Program to return most frequent character in a string
str1 = input("Enter String:")
#Here trying to form a key in dictionary and trying to find greatest value by using max function
ctr = {}
for x in str1:
    if x in ctr:
        ctr[x]+=1
    else:
        ctr[x]=1
res=max(ctr,key = ctr.get)
print("Frequent character present in the string is ", str(res))