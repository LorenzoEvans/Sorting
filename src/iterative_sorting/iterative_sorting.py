# TO-DO: Complete the selection_sort() function below 

def insertion_sort(arr):

    for i in range(0, len(arr)):
      # We generate a list of integers for every element in the array
        cur_val = arr[i]
      # We select the first value in the array
        index = i
      # We track out index placement with a variable i

        while index > 0 and arr[index - 1] > cur_val:
        # While our index is greater than 0, and the element in the array, located before our current index
        # is greater than our current value, we want to do some operations.
            arr[index] = arr[index - 1]
              # We want to replace whatever element is at our current index, with the one before it
            index -= 1
              # Then, we then subtract one from the index (why?)
                # Because we want to re-start the sort through the rest on the list, starting with the changed element,
                # in order to make sure we touch every item as we iterate.

        arr[index] = cur_val
        # If index is not greater than zero, OR the element located at our current array index is not greater than our current value,
        # We put the current value, at the index.

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