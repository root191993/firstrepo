
class A:

     def __init__(self):
        print("in A init")


     def feature1(self):
         print("Gopal")
     def feature2(self):
         print("Reddy")

class B:
     def __init__(self):
        print("in B init")
     def feature3(self):
         print("ji")
     def feature4(self):
         print("Pavan")

class C(A,B):

    def __init__(self):
        print("in C init")
        super().__init__()
        super().__init__()
        super().feature1()
        super().feature2()
    def feature5(self):
        print("Reddy")


c = C()




