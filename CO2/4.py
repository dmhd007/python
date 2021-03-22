import math
for i in range(1000,10000):
    if math.sqrt(i)%1==0:
        if int(i%10)%2==0:
            if int((i/10)%10)%2==0:
                if int((i/100)%10)%2==0:
                    if int((i/1000)%10)%2==0:
                        print(i)
# n=1532
# a=n%10
# print(a)
# b=int((n/10)%10)
# print(b)
# c=int((n/100)%10)
# print(c)
# d=int((n/1000)%10)
# print(d)