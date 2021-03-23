import csv
header = ["place","name","age"]
with open("city.csv","w") as file:
    write = csv.DictWriter(file,fieldnames=header)
    write.writeheader()
    write.writerow({"place": "vellimadukunnu", "name": "Aswin", "age": 21})
    write.writerow({"place": "Kakkodi", "name": "Dilshad", "age": 22})
    write.writerow({"place": "perindalmanna", "name": "Murshid", "age": 23})
with open("city.csv", "r") as file:
    read = csv.DictReader(file);
    n = input("Enter the column name you want(place,name,age):")
    for i in read:
        print(i[n])
