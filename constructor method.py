
class computer:

    def __init__(self,cpu,ram):  ## it is constructor method
        self.cpu = cpu
        self.ram = ram


    def config(self):  #  refers to the current object (instance) of the class.

# When you create an object, Python automatically passes that object as the first argument to instance method
        print("config is : ", self.cpu, self.ram)

com1 = computer("i5","16gb")
com2 = computer("i7","32gb")

com1.config()
com2.config()