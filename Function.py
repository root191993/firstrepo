

def person(name, **data):
    print(name)
    for i,j in data.items():
             print(i, j)
    
person("Pavan",  Age=33,  City="Adoni",  Mob=9880543812)