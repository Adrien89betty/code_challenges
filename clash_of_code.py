import sys
import math

f = 15
d = 25
r = 2

fuel_needed = f - (d * r)

if fuel_needed >= 0:
    print(fuel_needed)
else:
    print("not enough fuel")

