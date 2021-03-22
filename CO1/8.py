#8. Get a string from an input string where all occurrences of first character replaced with‘$’, except first character.
#\[eg: onion -> oni$n]
text1=str(input("Enter a word : "))
text2=text1
first=text1[0]
text1=text1.replace(first,"$")
text1=first+text1[1:]
print(text2,"-->",text1)