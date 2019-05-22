#Mark Boady
#CS260 - Homework 1 Binary Search Template

import math

def search(n,h):
    return bSearch(n, h, 0, len(h)-1)

def bSearch(n,h,start,stop):
    if stop < start:
        return False
    middle = math.floor((stop - start) / 2) + start
    print('Comparing element {} to needle {}'.format(h[middle], n))
    if h[middle] == n:
        return True
    elif n < h[middle]:
        return bSearch(n, h, start, middle - 1)
    else:
        return bSearch(n, h, middle + 1, stop)



#Do not make changes below this line.
import random
print("Welcome to Binary Search Test")
x=input("Enter Seed to Test:\n")
random.seed(x)
target=random.randint(0, 30)
list=[random.randint(0, 30) for x in range(0, 20)]
list.sort()
print("Looking for", target)
print("In list", list)
x = search(target, list)
if x==True:
    print("Target was found.")
else:
    print("Target was not found.")
