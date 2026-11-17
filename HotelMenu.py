
# Hotel menu



menu = {"pizza": 80,"Pasta": 50, "Salad": 70,"chapati": 45}
print(menu)
# Greet
print("Welcome to YSR Restaurant")
print("pizza: 80\nPasta: 50\nSalad: 70\nchapati: 45")

Order_Total = 0

item_1 = input("Enter your favourite item: ")
if item_1 in menu:
 Order_Total += menu[item_1]
 print(f"your favourite item is {item_1} is added to your order")
else:
 print(f"your favourite {item_1} is not in the menu")
another_order =  input("Do you want to add another order? (y/n): ")
if  another_order == "y":
    item_2 = input("Enter  add your favourite item: ")
    if item_2 in menu:
           Order_Total += menu[item_2]
           print(f"your favourite item is {item_2} is added to your order")
    else:
           print(f"your favourite {item_2} is not in the menu")
print(f"Your total order is {Order_Total}")



