# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        print('PREVIOUS LOWEST:')
        print(smallest_index)
        # TO-DO: find next smallest element
        for j in range(i, len(arr)):
            if(arr[j] < arr[smallest_index]):
                smallest_index = j
                print('NEW LOWEST:')
                print(smallest_index)

        # TO-DO: swap
        if(i != smallest_index):
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp
            print('NEW LIST')
            print(arr)

    return arr


print(selection_sort([7, 2, 9, 1, 3, 6, 0, 10]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr


print(bubble_sort([7, 2, 9, 1, 3]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
