n = int(input("Enter N  : "))

for x in range(1, n + 1):
    for y in range(1, x + 1):
        print(x * y, " ", end="")
    print()