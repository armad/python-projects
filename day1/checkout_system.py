# checkout_system.py
# This application calculates the checkout price for a local café.
# Author: Daniel Arce (armad)

name = input("What's your name? ")
number_coffees = int(input("How many coffees did you buy? "))
price = float(input("What's the price for each coffee? "))
TAX_RATE = 0.12

subtotal = round(number_coffees * price, 2)
total = round(subtotal + (subtotal * TAX_RATE), 2)

print("*" * 30)
print("\tRECEIPT\t\n")
print(f"Name: {name}\n")
print("Breakdown\n")
print("Qty\tItem\t\tCost")
print(f"{number_coffees}\t Coffee\t\t ${subtotal}\n")
print(f"Tax rate: {TAX_RATE * 100}%")
print(f"TOTAL: ${total}")
print("*" * 30)
