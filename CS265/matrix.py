
size = int(input("Enter size of Matrix: "))


A = [[0]*size]*size
B = [[0]*size]*size
C = [[0]*size]*size

for k in range(2):
    for i in range(size):
        for j in range(size):
            if k == 0:
                A[i][j] = int(input("Enter Value for Position A"+'['+str(i)+']['+str(j)+']  '))
            else:
                B[i][j] = int(input("Enter Value for Position B" + '[' + str(i) + '][' + str(j) + ']  '))

# # // Multiplying matrix a and b and storing in array mult.
for i in range(size):
    for j in range(size):
        C[i][j] = 0
        for k in range(size):
            C[i][j] += A[i][k] * B[k][j]

for i in range(size):
    for j in range(size):
        print(C[i][j])
