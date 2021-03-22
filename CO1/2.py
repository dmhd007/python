from datetime import date
todays_date = date.today()
currentYear=todays_date.year
finalYear=int(input("Enter final year : "))
q=finalYear+1
for x in range(currentYear,q):
  if x % 4 == 0:
    if x % 100 != 0:
      print(x)
  elif x%4 == 0:
    print(x)
