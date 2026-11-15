
import sys

sys.setrecursionlimit(200000)
sys.setrecursionlimit(100000)

i=0

def greet():
    global i
    print("hello",i)
    i=i+1
    greet()


greet()



