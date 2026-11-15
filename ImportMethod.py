from hashlib import algorithms_guaranteed
from os import name


class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    def show(self):
        print(self.name)
        print(self.age)
        self.lap.show()

    class Laptop:
         def __init__(self):
           self.brand = 'HP'
           self.cpu = "i5"
           self.ram = "4G"
         def show(self):
            print(self.brand)
            print(self.cpu)
            print(self.ram)



s1 = student(name="Pavan",age=20)
s2 = student(name="Reddy",age=25)

s1.show()
s2.show()
