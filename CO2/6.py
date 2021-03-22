dict={}
string=str(input("Enter a string : "))
for n in string:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
print(dict)