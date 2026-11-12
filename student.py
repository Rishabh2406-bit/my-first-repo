class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def Hi():
            print("Hello")
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi ",self.name," your average marks is:",(sum/3))

s1=Student("Rahul",[92,98,100])
s1.avg()
s1.name="Karan Ojhla" #if we want we can directly change the value by calling the desired function
s1.Hi()
s1.avg()

