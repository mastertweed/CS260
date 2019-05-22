# from math import ceil
# import time
#
# def partition(numbers, i, k):
#
#     midpoint = ceil(i + (k - i) / 2)
#     pivot = numbers[midpoint]
#
#     l = i
#     h = k
#
#     while l < h:
#
#         # if l != h:
#         # print('Compare {} to {}'.format(numbers[l], numbers[h]))
#
#         while (numbers[l] < pivot):
#             # print('{}, low: {}, high: {} , pivot: {}'.format(numbers,l,h,pivot))
#             # time.sleep(1)
#             l = l + 1
#
#         while (pivot < numbers[h]):
#             # print('{}, low: {}, high: {} , pivot: {}'.format(numbers,l,h,pivot))
#             # time.sleep(1)
#             h = h - 1
#
#         print('Compare {} to {}'.format(numbers[l], numbers[h]))
#
#         # time.sleep(1)
#         print(numbers)
#
#         if l < h:
#             numbers[l], numbers[h] = numbers[h], numbers[l]
#
#             l = l + 1
#             h = h - 1
#
#     return h
#
#
# def quickSort(numbers, i, k):
#
#     j = 0
#
#     if (i >= k):
#
#         return
#
#     j = partition(numbers, i, k)
#
#     quickSort(numbers, i, j)
#     quickSort(numbers, j + 1, k)



def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):

        # print(arr)
        print('Compare {} to {}'.format(arr[j],pivot))

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


#Test Area - Do not edit below this line
import random
print("Quick Sort Test Question")
x = int(input("Enter Seed for Testing:\n"))
random.seed(x)
test_size = int(input("Enter Test Size:\n"))
L = [random.randint(0,50) for x in range(0,test_size)]

# test_size = 4
# L = [7,4,6,18,8]

print("Quick Sorting List")
print("Initial List:",L)
quickSort(L,0,test_size-1)
print("Final List:",L)
