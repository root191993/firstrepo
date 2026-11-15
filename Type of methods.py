

class  student():

   School = "Telusko"
   def __init__(self,s1,s2,s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

   def get_m1(self):
        return self.s1
   def get_m2(self):
        return self.s2
   def get_m3(self):
       return self.s3


   def avg(self):
    return (self.s1 + self.s2 + self.s3)/3
   def sum(self):
         return self.s1 + self.s2 + self.s3
   def sub(self):
       return self.s1 - self.s2
   def mul(self):kk
       return self.s1*self.s2
   def div(self):
       return self.s1/self.s2
   @classmethod
   def  getschool(cls):
        return cls.School
   @staticmethod
   def info():
     print("Hi How are you")
s1 = student(45,55,78)
s2 = student(78,45,54)

print(s1.avg())
print(s2.avg())
print(student.getschool())
print(s1.sub())
print(s2.sub())
print(s1.mul())
print(s2.mul())
print(s1.div())
print(s2.div())

student.info()