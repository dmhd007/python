s = str(input("Enter a line of text : "))
counts = dict()
words = s.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)