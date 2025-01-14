
# This Python code simulates a simple restaurant ordering system. Here's a breakdown of what the code
# does:
menu={
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Momo":50
}

print("Welcome to Our Restaurant")
print("Pizza = Rs 40\n""Pasta =Rs 50\n""Burger = Rs 60\n""Momo = Rs 50")
order_total=0
item_1=input("Enter Your order")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} is ordered")
else:
    print(f"order{item_1}is not available")
another_order=input("Do you want to add other order?")
if another_order=="yes":
    item_2=input("Enter the name of your order")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"The item {item_2} is not available")
print(f"The total amount of items to pay is {order_total}")
