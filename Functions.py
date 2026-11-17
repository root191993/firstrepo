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

def display_invoice(username, amount, due_date):
    print(f"Your invoice is {username}")
    print(f"You pay amount ${amount} ")
    print(f"Due date is {due_date}")

display_invoice("Pavan", 1200, "01/09/1993")
display_invoice("Siri", 1500, "21/112023")
display_invoice("Gagana", 2000, "20/02/2020")

def create_name(first, last):
     first = first.capitalize()
     last = last.capitalize()
     return f"{first} {last}"

full_name = create_name("Pavan", "Reddy")
print(full_name)




