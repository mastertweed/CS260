def InsertionSort(A):
    for j in range(1,len(A)):
        flag = 0
        for i in range(j,0,-1):
            if flag == 0:
                print("Compare {} to {}".format(A[i-1],A[i]))
                if A[i] < A[i-1]:
                    temp = A[i]
                    A[i] = A[i-1]
                    A[i-1] = temp
                else:
                    flag = 1


#Test Area - Do Not make changes below this line.
import random
print("Insertion Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Insertion Sorting List")
print("Initial List:",L)
InsertionSort(L)
print("Final List:",L)
