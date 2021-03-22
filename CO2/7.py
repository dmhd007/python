string=str(input("Enter a string : "))
if string[-3:]=="ing":
    print(string.__add__("ly"))
else:
    print(string.__add__("ing"))