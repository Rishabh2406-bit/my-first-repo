class Account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no

    def debit(self,amount):
        self.bal-=amount
        print("Rs",amount," was debited")
    def credit(self,amount):
        self.bal+=amount
        print("Rs",amount," was debited")
    def Final_bal(self):
        print("The final amount in the account is:",self.bal)

acc1=Account(100000, 12345)
print(acc1.bal)
print(acc1.acc_no)
acc1.debit(2000)
acc1.credit(1500)
acc1.Final_bal()

