import math

def T(n):
    if n == 1:
        return n
    else:
        return 2 * T(n / 2) + n

print('Analysis of First Recursive Function')

in1 = int(input('Enter starting power of 2:\n'))
in2 = int(input('Enter final power of 2:\n'))


print('%10s %10s %10s %10s %10s' % ("n", "T(n)", "n lg n", "1/2n^2", "n^2"))
for i in range(in1,in2+1):
    n = 2**i
    print('%10d %10d %10d %10d %10d' % (n, T(n), n * math.log(n,2), 1/2 * n**2, n**2))