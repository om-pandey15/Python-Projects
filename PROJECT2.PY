# Define the menu of restaurant
menu = {
    "pizza": 100,
    "pasta": 50,
    "burger": 60,
    "salad": 40,
    "soda": 20,
}

# Greet the customer
print("Welcome to Python Restaurant!")
print ("Pizza: Rs 100\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 40\nSoda: Rs 20")

order_total = 0
item_1 = input("Enter the name of the first item you want to order: ")
#Memebership operator to check if the item is in the menu
if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} has been added to your order.")
else:
    print("Invalid item. Please try again.")
another_order = input("Do you want to order another item? (yes/no): ")
if another_order == "yes":
    item_2 = input("Enter the name of the second item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} has been added to your order.")
    else:
        print("Invalid item. Please try again.")
print(f"Your total bill is: Rs {order_total}") 