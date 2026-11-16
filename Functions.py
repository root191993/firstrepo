numbers = [1,2,3,4,5,6,7,8,9,10]
result = []
for n in numbers:
    result.append(n*n)
print(result)

# function() reuseble the block of code

def Happy_birthday(name, age):
    print(f"Happy Birthday TO {name}")
    print(f"You are {age} years old")
    print("Happy Birthday TO you")
    print()


Happy_birthday("Pavan", 33)
Happy_birthday("Siri", 3)
Happy_birthday("Gagana", 6)
