
a = 5
b = 2

try:
    print("Resorce Open")
    print(int(a/b))
    print("Resource Closed")
    k = int(input("Enter a number: "))
    print(k)
except ZeroDivisionError as e:
    print("Hey you can't divide a Number by Zero",e)
    print("Resource closed")
except ValueError as e:
    print("invalid input", e)
except TypeError as e:
    print("Typo Error", e)
except NameError as e:
    print("name error", e)
except Exception as e:
    print("Something bad happened", e)