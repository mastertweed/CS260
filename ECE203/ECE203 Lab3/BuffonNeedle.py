from random import random
from math import pi, sin

user = int(input('Attempts to perform\n'))
hit = 0

for i in range(user):
    y_tail = 2*random()
    angle = sin(random()*pi)
    print(y_tail+angle)
    if y_tail + angle > 2:
        hit = hit+1

print(user,':',hit)