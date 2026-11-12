# #A normal class and obejct program
# class Student:
#     name="Rishabh"

# ob1=Student()
# print(ob1)
# print(ob1.name)

#A constructor is always invoked even if no consructor is present and if we want to add a constructor we can define it using init function

class Cars:
    def __init__(self,name,color):
        self.name=name #self is always the fisrt argument
        self.color=color
        print("Adding new details to a car")
    brand="Mercedes"
Car1= Cars("A_Class","Blue")
print(Car1.name)
print(Car1.color)
print(Car1.brand)

Car2= Cars("G-Class","Red")
del Car2 #It can delete an entire object or just an attribute of it
print(Car2.name)
print(Car2.color)
print(Car2.brand)