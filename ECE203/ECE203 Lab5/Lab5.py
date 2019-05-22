
def fib(n):
    seq = []
    for i in range(n):
        seq.append(0)

    for i in range(n):
        if i == 0 or i == 1:
            seq[i] = 1
        else:
            seq[i] = seq[i-1] + seq[i-2]

    return seq

for i in fib(10):
    print(i)

# ----------

mat = [[10, 20, 30, 40, 50, 60],
     [11, 21, 31, 41, 51, 61],
     [12, 22, 32, 42, 52, 62],
     [13, 23, 33, 43, 53, 63],
     [14, 24, 34, 44, 54, 64],
     [15, 25, 35, 45, 55, 65],
     [16, 26, 36, 46, 56, 66]]

# Print each row (iteration) of mat
for row in mat:
    print(row)

# For each row for the amount of rows of the matrix, create a new row of elements i in j row.
trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print("\n")
for row in trans:
    print(row)
