# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math


def merge(arrA, arrB):
    merged_arr = []
    # TO-DO
    i = 0
    j = 0
    while(i < len(arrA) and j < len(arrB)):
        if(arrA[i] > arrB[j]):
            merged_arr.append(arrB[j])
            j += 1
        elif(arrB[j] > arrA[i]):
            merged_arr.append(arrA[i])
            i += 1
    while(i < len(arrA)):
        merged_arr.append(arrA[i])
        i += 1
    while(j < len(arrB)):
        merged_arr.append(arrB[j])
        j += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if (len(arr) <= 1):
        return arr
    middle = math.floor(len(arr)/2)
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    arr = merge(left, right)
    return arr

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# def mergeSort(arr1, arr2):
#     results = []
#     i = 0
#     j = 0
#     while(i < len(arr1) and j < len(arr2)):
#         if(arr1[i] > arr2[j]):
#             results.append(arr2[j])
#             j += 1
#         elif(arr2[j] > arr1[i]):
#             results.append(arr1[i])
#             i += 1
#     while(i < len(arr1)):
#         results.append(arr1[i])
#         i += 1
#     while(j < len(arr2)):
#         results.append(arr2[j])
#         j += 1

#     return results


# print(mergeSort([1, 3, 6, 9], [2, 5, 10, 12, 16]))
