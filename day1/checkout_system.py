# checkout_system.py
# This application calculates the checkout price for a local café.
# Author: Daniel Arce (armad)

name = input("What's your name? ")
number_coffees = int(input("How many coffees did you buy? "))
price = float(input("What's the price for each coffee? "))
TAX_RATE = 0.12

subtotal = number_coffees * price
tax = subtotal * TAX_RATE
total = subtotal + tax

print("*" * 30)
print("\tRECEIPT\t\n")
print(f"Name: {name}\n")
print("Breakdown\n")
print("Qty\tItem\t\tCost")
print(f"{number_coffees}\t Coffee\t\t ${subtotal:.2f}\n")
print(f"Sales tax: ${tax:.2f}")
print(f"TOTAL: ${total:.2f}")
print("*" * 30)
