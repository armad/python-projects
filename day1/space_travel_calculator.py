# digital_id_card.py
# Script to calculate travel times to the moon.
# Author: Daniel Arce (armad)

distance = 384400
speed = 5000
time = distance / speed

print(f"At speed of {speed} km/h, it will take {time} hours to reach the moon.\n")

# Time needs to change to a higher value (e.g. 15,000).
print(
    f"At speed of {speed:= 10000} km/h, it will take {time} hours to reach the moon.\n"
)

time = 24
remaining_distance = distance % time

print(f"After {time} hours, the remaining distance is {remaining_distance}")
