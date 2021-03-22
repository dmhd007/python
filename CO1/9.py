word=str(input("Enter a string : "))
word1=word
word=word[-1:]+word[1:-1]+word[:1]
print(word1,"-->",word)

