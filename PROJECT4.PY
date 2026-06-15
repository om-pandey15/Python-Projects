rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total amount of  electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of person living in room or flat"))

total_bill = electricity_spend * charge_per_unit

output = (rent + food + total_bill) / persons

print("Each person should pay:", output)