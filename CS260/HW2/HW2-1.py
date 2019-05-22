
def BubbleSort(A):

    flag = 0
    while flag == 0:
        flag = 1
        for i in range(len(A)-1):
            print("Compare {} to {}".format(A[i],A[i+1]))
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                flag = 0

#Test Area - Do Not make changes below this line.
import random
print("Bubble Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Bubble Sorting List")
print("Initial List:",L)
BubbleSort(L)
print("Final List:",L)