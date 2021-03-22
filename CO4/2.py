class Bank:
    def __init__(self,member,accno,type,balance):
        self.member=member
        self.type=type
        self.accno=accno
        self.balance=balance
    def deposit(self):
        damount=int(input("Enter the amount to be deposit : "))
        self.balance=self.balance+damount
        print("Amount is successfully deposited.")
        print("Your available balance is :",self.balance)
    def withdraw(self):
        wamount=int(input("Enter the amount to be withdraw : "))
        if(self.balance<wamount):
            print("Insufficient balance")
        else:
            self.balance=self.balance-wamount
            print("Amount is successfully Withdrawed.")
            print("Your available balance is :",self.balance)

c1=Bank("aswin",2020,"current",7500)
c2=Bank("dilshad",2021,"savings",5000)
dep1=c1.deposit()
# dep2=c2.deposit()
with1=c1.withdraw()
# with2=c2.withdraw()