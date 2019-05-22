import math


def MergeSort(arr):
    if len(arr) > 1:
        mid = math.ceil(len(arr) / 2)
        # mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        # print(L)
        # print(R)

        MergeSort(L)  # Sorting the first half
        MergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print('Compare {} to {}'.format(R[j],L[i]))
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#Test Area - Do not make changes below this line
import random
print("Merge Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

print("Merge Sorting List")
print("Initial List:",L)
MergeSort(L)
print("Final List:",L)
