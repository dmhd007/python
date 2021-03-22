limit=int(input("Enter the limit : "))
list1=[]
list2=[]
for x in range(0,limit):
  item=int(input("Enter the integer : "))
  list1.append(item)
for i in list1:
  if i%2!=0:
    list2.append(i)
print("The complete list is :",list1)
print("The list after removing even number is :",list2)