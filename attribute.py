#self in the case is an instance attribute for every different objects

class Student:
    college_name="ABC Collage"  #Class attribute
    def __init__(self,name,age):
        self.name=name   #Instance attribute
        self.age=age
    def welcome(self):
        print("Welcome dear student ,", self.name)

s1=Student("Karan",18)
s1.welcome()
print(s1.college_name , s1.name , s1.age)

s2=Student("Rishabh",19)
s2.welcome()
print(s2.college_name , s2.name , s2.age)