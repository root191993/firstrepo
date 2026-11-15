class student:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
      m1 = self.m1 + other.m1
      m2 = self.m2 + other.m2
      m3 = student(m1,m2)
      return m3




    def __gt__(self, other):
        m1 = self.m1 + self.m1
        m2 = other.m2 + other.m2
        if  m1 > m2:
            return True
        else:
          return False
    def __str__(self):
        return  '{} {}'.format(self.m1,self.m2)




s1 = student(50,45)
s2 = student(55,48)

if s1 > s2:
    print("Hello")
else:
    print("Hi")

a = 2

print(a)
print(s1)
print(s2)


