from itertools import islice

class Topten:
    def __init__(self, iterable):
        self.iterable = 1
    def __iter__(self):
        return self
    def __next__(self):

        if self.iterable <= 10:
           value = self.iterable
           self.iterable += 1
           return value
        else:
          raise StopIteration
values = Topten(iterable=1)
print(next(values))
for value in values:
    print(value)



