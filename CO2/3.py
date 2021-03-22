limit=int(input("Enter the limit : "))
list1=[]
sum=0
for x in range(0,limit):
  item=int(input("Enter the item : "))
  list1.append(item)
print("The list is :",list1)
for i in range(0,len(list1)):
  sum=sum+list1[i]
print("The sum is :",sum)