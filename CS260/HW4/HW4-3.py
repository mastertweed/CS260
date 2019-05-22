import math

total = 0
def T(n,a,b,x,y):
    if n <= 1:
        return 1
    else:
        return a*T((math.floor(n/b)),a,b,x,y) + (n**x) * math.ceil(math.log2(n)**y)

print('General Recursion Example')
a = int(input('Enter Value for a:\n'))
b = int(input('Enter Value for b:\n'))
x = int(input('Enter Value for x:\n'))
y = int(input('Enter Value for y:\n'))
n = int(input('Enter Value for n:\n'))

print('Evaluating {}T(n/{})+n^{} log2(n)^{}'.format(a,b,x,y))
print('T({})={}'.format(n,T(n,a,b,x,y)))

