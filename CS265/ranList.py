import sys
import random

# sys.argv[1] == x, sys.argv[2] == n
x = int(sys.argv[1])

vec = list()
for i in range(x):
    vec.append(random.randint(0, 1000000))
    print(vec[i])