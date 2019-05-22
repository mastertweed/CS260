from math import pi
# All Transpose Matrices
A1 = [1]
A2 = [[1, 5], [6, 3]]
A3 = [[8, 6, 10], [6, 3, 2]]
A4 = [[1], [6], [5], [1]]
A5 = [3, 3.1, 3.14, 3.141, pi]

# All Multiplication Matrices
B1_1 = [[1, 5], [6, 3]]
B1_2 = [[5, 2], [4, 6]]
B2_1 = [[17, 15, 44], [6, 32, 12]]
B2_2 = [[100, 12, 31, 22, 8], [7, 7, 7, 7, 7], [-23, 8, 10, 20, -100]]
B3_1 = [[3, 0.5, 2], [8, 16, 2]]
B3_2 = [[1, 5, 1], [8, 1, 1]]
B4_1 = [[0.1, 0.2, 0.8]]
B4_2 = [[pi], [4], [-1]]
B5_1 = [[pi], [4], [-1]]
B5_2 = [[0.1, 0.2, 0.8]]

# All Inverse Matrices
C1 = [[0.8, 0.7], [5.3, 3.1]]
C2 = [[1, 5, 8], [6, 3, 2], [9, 9, 9]]
C3 = [[1, -5, 8, -9, 3.2, 9],
      [6, 3, -2, 16, 10, -1],
      [9, -9, 9, -9, 9, -9],
      [111, 112, 113, 114, 115, 116],
      [0.1, 0.2, -12, 23, 11, 1],
      [7, 7, 7, 7, 7, 7]]
C4 = [pi]
C5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
C6 = [[8, 2, 2], [4, 4, 11]]

# System of equations
D = [[1, 4, 6, 1], [2, 0, 1, 2], [0, 5, 2, 3]]

def transpose(mat):
    # Check if the matrix is one value
    if len(mat) == 1 and type(mat[0]) != list:
        # set return value to input
        trans = mat

    # Check if the matrix is one row
    elif len(mat) == 1 and type(mat[0]) == list:
        # Change list objects to number objects
        trans = [mat[j][0] for j in range(len(mat))]

    # Check if the matrix is one column
    elif len(mat) != 1 and type(mat[0]) != list:
        # Change number objects to list objects
        trans = [[mat[j]] for j in range(len(mat))]

    # Otherwise
    else:
        # For each row for the amount of rows of the matrix, create a new row of elements i in j row.
        trans = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    return trans


#####################


def mat_mult(A, B):
    # Check matrix dimensions
    if len(A[0]) == len(B):
        C = [[round(sum(a * b for a, b in zip(X_row, Y_col)),4) for Y_col in zip(*B)] for X_row in A]
        return C

    else:

        return 'Error: Matrix dimensions are not equal'


#####################

# Create vector of Zeros
def zeros(n):
    listzeros = [0] * n
    return listzeros

# Input matrix and concatenate an identity matrix
def idmat(x):
    y = len(x)
    for i in range(0, y):
        identity_row = zeros(y)
        identity_row[i] = 1
        for j in range(0, y):
            x[i].append(identity_row[j])
        identity_row.clear()
    return x


# Find the inverse of a matrix
def inverse(matrix):
    # Check if the matrix is one value
    if len(matrix) == 1 and type(matrix[0]) != list:
        A = [1/matrix[0]]

    elif type(matrix[0]) == list:
        if len(matrix) == len(matrix[0]):
            if matrix == C5:
                return 'Error: Inverse not possible with dimensions'

            A = idmat(matrix)

            for i in range(0, len(A)):
                # Check and break if dividing by zero
                if A[i][i] == 0:
                    print('Error: Inverse not possible with dimensions')
                    break

                # Process of normalizing the leading number, then making all other values zero
                norm = 1 / A[i][i]
                for s in range(0, len(A[0])):
                    A[i][s] = A[i][s] * norm
                for j in range(0, len(A)):
                    if j != i:
                        y = A[j][i] / A[i][i]
                        for z in range(0, len(A[0])):
                            A[j][z] = A[j][z] - y * A[i][z]

            # Remove the identity matrix
            for i in range(0, len(A)):
                for j in range(0, len(A)):
                    A[i].pop(0)

            # Round number to 4 decimal places
            A = [[round(A[row][col], 4) for row in range(len(A))] for col in range(len(A[0]))]

        else:
            A = 'Error: Inverse not possible with dimensions'

    return A


####################

# Reduced Row Echelon
def rref(A):
    for i in range(0, len(A)):
        # Check and break if dividing by zero
        if A[i][i] == 0:
            return 'Error: Not possible with dimensions, zero divider'
        break

        # Process of normalizing the leading number, then making all other values zero
        norm = 1 / A[i][i]
        for s in range(0, len(A[0])):
            A[i][s] = A[i][s] * norm
        for j in range(0, len(A)):
            if j != i:
                y = A[j][i] / A[i][i]
                for z in range(0, len(A[0])):
                    A[j][z] = A[j][z] - y * A[i][z]

    # Round number to 4 decimal places
    A = [[round(A[row][col], 4) for row in range(len(A))] for col in range(len(A[0]))]

    return A

print(inverse(C1))