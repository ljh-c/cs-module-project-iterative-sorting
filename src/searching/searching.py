def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # array must be sorted
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            # toss out low side of array
            low = mid + 1
            continue
        
        if arr[mid] > target:
            # toss out high side of array 
            high = mid - 1
            continue

    return -1  # not found
