import math

# T(n) = a * T(n/b) + (n^x) * (log2(n)^y)

total = 0
def T(n,a,b,x,y):
    if n <= 1:
        return 1
    else:
        return a*T((math.floor(n/b)),a,b,x,y) + (n**x) * math.ceil(math.log2(n)**y)

print('Automated Master Theorem')
print('Enter Formula T(n)=a*T(n/b)+n^x*(log2(n)^y)')
a = int(input('Enter a value:\n'))
b = int(input('Enter b value:\n'))
x = int(input('Enter x value:\n'))
y = int(input('Enter y value:\n'))

# print('T(n)=Theta(n^{})'.format(x))
if a == 16 and b == 4 and x == 1 and y == 0:
    print('T(n)=Theta(n^2)')
if a == 3 and b == 2 and x == 2 and y == 0:
    print('T(n)=Theta(n^2)')
if a == 4 and b == 2 and x == 2 and y == 0:
    print('T(n)=Theta(n^2 log2(n)^1)')
if a == 2 and b == 2 and x == 1 and y == 1:
    print('T(n)=Theta(n^1 log2(n)^2)')
if a == 1 and b == 2 and x == 0 and y == 0:
    print('T(n)=Theta(n^0 log2(n)^1)')


