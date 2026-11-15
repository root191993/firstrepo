# total rent
# total food
# Electricity units spend
# Charge per unit
# Persons living in room/Flat
## Output
# Total amount you have pay


rent = int(input("Enter the rent amount: "))
food = int(input("Enter the food amount: "))
Eus = int(input("Enter the eus amount: "))
CPU = int(input("Enter the CPU amount: "))
Person = int(input("Enter the number of persons: "))
TB = Eus * CPU

Output = (rent + food + TB) // Person

print("you have to pay each:", Output)
