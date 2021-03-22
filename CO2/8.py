list1=[]
limit=int(input("Enter the number of words : "))
for i in range(0,limit):
    word=str(input("Enter Word : "))
    list1.append(word)
max=len(list1[0])
temp=list1[0]
for j in list1:
    if(len(j)>max):
        max=len(j)
        temp=j;
print("The word with longest length is : "+temp+" and length is :",max)
# print(list1)
