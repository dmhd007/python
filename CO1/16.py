str1=str(input("Enter 1st string : "))
str2=str(input("Enter 2nd string : "))
newstr1=str2[:1]+str1[1:]
newstr2=str1[:1]+str2[1:]
print(newstr1+" "+newstr2)