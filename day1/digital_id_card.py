# digital_id_card.py
# This application generates a text-based "ID card" for a user.
# Author: Daniel Arce (armad)

name = input("What's your name? ")
age = int(input("What's your age? "))
height = float(input("What's your height? "))
is_premium = bool("True")

# We need asterisks to make it seem like a nicely formatted digital card.

print("*" * 15)
print("DIGITAL ID CARD\n")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Premium Status: {is_premium}\t")
print("*" * 15)
