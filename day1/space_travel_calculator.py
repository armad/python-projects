# space_travel_calculator.py
# Script to calculate travel times to the moon.
# Author: Daniel Arce (armad)

distance = 384400
speed = 5000
time = distance / speed

print(f"At speed of {speed} km/h, it will take {time} hours to reach the moon.\n")

speed = 10000
time = distance / speed

print(f"At speed of {speed} km/h, it will take {time} hours to reach the moon.\n")

distance_24h = distance / 24
remaining_distance = distance - distance_24h

print(f"After 24 hours, the remaining distance is {remaining_distance}.")
