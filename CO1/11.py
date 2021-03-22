a = int(input ("Enter 1st number "))
b = int(input ("Enter 2nd number "))
c = int(input ("Enter 3rd number "))
if a > b:
  if a > c:
    print(a," is Largest")
  else:
    print(c," is Largest")
else:
  if b > c:
    print(b," is Largest")
  else:
    print(c," is Largest")