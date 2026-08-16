# digital_id_card.py
# This application generates a text-based "ID card" for a user.
# Author: Daniel Arce (armad)

name = input("What's your name? ")
age = int(input("What's your age? "))
height = float(input("What's your height? "))
is_premium = True

# 15 asterisks to match the max lenght of each line.

print("*" * 20)
print("DIGITAL ID CARD\n")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Premium Status: {is_premium}\n")
print("*" * 20)
