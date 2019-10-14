import random
import numpy

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

size = int(input("Enter Size of Array: "))
A1 = list()
for i in range(size):
    print("Enter Value for A[",i,"]")
    s = int(input())
    A1.append(s)

print("Input: " + str(A1))
quickSort(A1, 0, len(A1) - 1)
print("Output: " + str(A1))
print(" ")