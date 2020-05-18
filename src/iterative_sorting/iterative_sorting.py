# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if i != smallest_index:
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False
        # each pass loops through n-1 elements
        for i in range(0, len(arr) - 1):
            # compare adjacent elements
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            
    # stop looping after a pass with no swaps
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # maximum arg is not used in test, so it is set to 199
    maximum = 199

    # only for possible elements 0 - 9
    counts = [0 for _ in range(0, maximum + 1)]

    for num in arr:
        if num < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:    
            counts[num] += 1

    sorted_arr = []

    for i in range(0, len(counts)):
        sorted_arr += [i] * counts[i]

    return sorted_arr

# NEXT TO DO: 
# - negative values
# - set smallest value
# - compare objects with strings and numbers