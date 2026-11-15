from operator import truediv


class computer:
    def __init__(self):
        self.name = "Pavan Kumar"
        self.age = 33

    def compare(self,other):
       if self.age == other.age:

           return True
       else:
           return False


c1 = computer()
c1.name = "Reddy"
c2 = computer()
c1.compare(c2)

if c1.compare(c2):  # compare() function is comparring the two objects
    print("it is same")
else:
    print("it is different")

print(c1.compare(c2))
print(c2.name)  ## self it is referring the object 
print(c1.age)