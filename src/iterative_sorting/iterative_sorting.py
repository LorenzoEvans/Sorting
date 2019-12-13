# TO-DO: Complete the selection_sort() function below 

# def insertion_sort(arr):
#     for i in range(0, len(arr)):
#         cur_val = arr[i]
#         print(cur_val)
#         index = i
#         print("Outer index:", index)
#         while index > 0 and arr[index - 1] > cur_val:
#             arr[index] = arr[index - 1]
#             index -= 1
#             print("Inner index:", index)
#         arr[index] = cur_val
#     return arr

#  Conceptually, we split a collection into sorted and unsorted parts.
#  One part is the first element, and a single element list is always sorted.
def insertion_sort(arr):
    for i in range(0, len(arr)):  # Every number between 0 and length of data set
        cur_val = arr[i]  # Capture array element selected on current iteration of for loop
        #print(cur_val)  # Printing for check
        index = i  # Set index to number indication which iteration is currently taking place
        #print("Index is:", index, "i is: ", i)
        while index > 0 and arr[index - 1] > cur_val:  # While index > 0 & the element of the arr at the index equaling index - 1 is greater than the current element
            #  arr[index - 1] doesn't trigger out of bounds because python lists loop around at -1, and 0 - 1 == -1
            arr[index] = arr[index - 1]  # set the current element to the value before it, because the current element is less than the previous one.
            index -= 1
        print(arr[index - 1])
        arr[index] = cur_val


rand_arr = [1, 4, 6, 12, 5, 2]

def insertion_sort(arr):
    for i in range(0, len(arr)):
        cur_val = arr[i] # arr[i => (0)] => 1 # arr[i => (1)] => 4
        index = i # index => 0 # index => 1
        while index > 0 and arr[index - 1] > cur_val:
	    # while 0 > 0 and arr[index (0) - 1 => -1 => (2)] 2 > 1
	    # while 1 > 0 and arr[index (1) - 1 => 0] => 1 > 4
	    # bc both false, 1 and two are *not* swapped.
	    # bc one false, nothing swapped, index not decremented
            arr[index] = arr[index - 1]
            index -= 1
        print(arr[index - 1])
        arr[index] = cur_val


print(insertion_sort(rand_arr))

# for i in range(0, len(rand_arr)):
# 	print(i)

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
