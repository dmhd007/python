limit1 = int(input("Enter the limit for list 1 : "))
limit2 = int(input("Enter the limit for list 2 : "))

list1 = []
list2 = []
sum1 = 0
sum2 = 0
result = 0

for x in range(0, limit1):
    item1 = int(input("Enter the item for list 1 : "))
    list1.append(item1)
for y in range(0, limit2):
    item2 = int(input("Enter the item for list 2 : "))
    list2.append(item2)
print("The list 1 is :", list1)
print("The list 2 is :", list2)

length1 = len(list1)
length2 = len(list2)

if length1 == length2:
    print("List 1 and List 2 are of same length")
else:
    print("list 1 and List 2 are of diffrent length")
for p in range(0, length1):
    sum1 = sum1 + list1[p]
print("The sum of List 1 is :", sum1)

for q in range(0, length2):
    sum2 = sum2 + list2[q]
print("The sum of List 2 is :", sum2)
if sum1 == sum2:
    print("Sum of List 1 and List 2 are same")
else:
    print("Sum of List 1 and List 2 are not same")

for a in list1:
    for b in list2:
        if a == b:
            result = 1
if result == 1:
    print("Same value occur in both lists")
else:
    print("Same value not occur in both lists")