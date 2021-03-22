limit=int(input("Enter the limit : "))
list1=[]
for x in range(0,limit):
  item=int(input("Enter the item : "))
  if item >= 100:
    list1.append('over')
  else:
    list1.append(item)
print("The list is :",list1)
