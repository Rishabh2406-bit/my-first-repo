class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #by adding two underscore infront of the variable name it will make that variable private
    def reset_pass(self):
        print(self.__acc_pass) #this statement will work because it is inside the class
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass()) #it wont give an error now

print(acc1.__acc_pass) #but this statement wont work cause its not in the class