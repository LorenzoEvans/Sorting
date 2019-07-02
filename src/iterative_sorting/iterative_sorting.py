# TO-DO: Complete the selection_sort() function below 

def insertion_sort(arr):
    for i in range(0, len(arr)):
        cur_val = arr[i]
        print(cur_val)
        index = i
        print("Outer index:", index)
        while index > 0 and arr[index - 1] > cur_val:
            arr[index] = arr[index - 1]
            index -= 1
            print("Inner index:", index)
        arr[index] = cur_val
    return arr


rand_arr = [1, 4, 6, 12, 5, 2]

print(insertion_sort(rand_arr))

# def selection_sort( arr ):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = 0
#         # first element of arr
#
#         smallest_index = cur_index
#
#         while smallest_index > cur_index:
#
#
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#
#
#
#
#         # TO-DO: swap
#
#
#
#
#     return arr
#
#
# # TO-DO:  implement the Bubble Sort function below
# def bubble_sort( arr ):
#
#     return arr
#
#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr