# checkout_system.py
# This application calculates the checkout price for a local café.
# Author: Daniel Arce (armad)

name = input("What's your name? ")
number_coffees = int(input("How many coffees did you buy? "))
price = float(input("What's the price for each coffee? "))
TAX_RATE = 0.12

subtotal = number_coffees * price
total = subtotal + (subtotal * TAX_RATE)
