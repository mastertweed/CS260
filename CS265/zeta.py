import sys

# sys.argv[1] == x, sys.argv[2] == n
# x = int(sys.argv[1])
# n = int(sys.argv[2])
# total = 0
#
# for i in range(n):
#     total = total + (1/(i+1))**x
#
# print('z(', n, ')=', round(total,7), 'when approximated at n=', n)
print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

A1 = list()
for i in range(size):
    A1.append(sys.argv[i+1])