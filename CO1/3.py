#(a) Generate positive list of numbers from a given list of integers
list1=[1,2,-2,4,-3,0,-7-14]
positiveList=[x for x in list1 if x>0]
print(positiveList)

#(b) Square of N numbers
limit=int(input("Enter the limit : "))
list2=[]
for i in range(limit):
  i=int(input("Enter number : "))
  list2.append(i)
print(list2)
squareList=[x*x for x in list2 ]
print(squareList)

#(c) Form a list of vowels selected from a given word
word="comprehension"
vowels="aeiou"
list3=[x for x in word if x in vowels]
print(list3)

#(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
word2="flower"
list4=[ord(x) for x in word2]
print(list4)
