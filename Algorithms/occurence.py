# def occurence_count(arr, target):  #linear searching
    # count = 0
    # for i in range (len(arr)):
        # if arr[i] == target:
            # count = count+1
    # return count

# arr = [1, 2, 2, 3, 2, 4]
# target = 2
# print(occurence_count(arr,2))

#binary searching
def occ_countBi(arr, target):
    low = 0
    high = len(arr) - 1
    first = -1
    last = -1

    # First occurrence
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Reset for last occurrence
    low, high = 0, len(arr) - 1

    # Last occurrence
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return (first, last)


# Test
arr = [1, 2, 2, 2, 3, 3, 3, 3, 4]
target = 2
print(occ_countBi(arr, target))
