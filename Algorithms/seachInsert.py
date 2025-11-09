def search_insert(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid ] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

# Test
arr = [10, 20, 30, 40, 50]
target = 35
print(search_insert(arr, target))  # Expected Output: 3doned 