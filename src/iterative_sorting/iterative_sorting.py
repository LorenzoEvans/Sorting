# TO-DO: Complete the selection_sort() function below 

def insertion_sort(arr):

    for i in range(0, len(arr)):
      # We generate a list of integers for every element in the array
        cur_val = arr[i]
      # We select the first value in the array
      # This establishes a helpful baseline for orderliness, as a single element list is already perfectly ordered.
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
              # This is "iterating to the left", by decreasing the index of the sorted array
              # to target indexes in the sorted "single" element

        arr[index] = cur_val
        # If index is not greater than zero, OR the element located at our current array index is not greater than our current value,
        # We put the current value, at the index.

    return arr


rand_arr = [1, 4, 6, 12, 5, 2]

# print(insertion_sort(rand_arr))

def selection_sort( arr ):

  for x in range(len(arr)):
    min_idx = x
    print("x is: ", x)
    for y in range(x + 1, len(arr)):
      # Progressively shortens the section of the unsorted array to search
      print("y is: ", y)
      if arr[min_idx] > arr[y]:
        # if the element at current index, is greater than the element following
        # it, set min_idx to j (which equals (i + 1))
        min_idx = y
    print("arr is: ", arr)
    arr[x], arr[min_idx] = arr[min_idx], arr[x]
  return arr

print(selection_sort([64, 25, 12, 22, 11]))


#
#
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  n = len(arr) # Get length of array.
  
  for i in range(n):
    for j in range(0, n - (i - 1)):
      if arr[j] > arr[j + 1]:
          arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr
#
#
# # STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):
#
#     return arr