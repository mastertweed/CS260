def T(n):
    count = 0
    for i in range(n):
        j = i
        while j < n:
            count += 1
            j += 1

    return count


print('Analysis of Double Nested Loop')

in1 = int(input('Enter Starting Power of 2:\n'))
in2 = int(input('Enter Final Power of 2:\n'))


print('%10s %10s %10s %10s %10s' % ("n", "T(n)", "1/2n^2", "n^2", "2n^2"))
for i in range(in1,in2+1):
    n = 2**i
    print('%10d %10d %10d %10d %10d' % (n, T(n), 1/2*n**2, n**2, 2*n**2))