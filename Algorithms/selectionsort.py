def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_id = i
        for j in range(i+1,n):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[i], arr[min_id] = arr[min_id], arr[i]

    return arr

arr = [64,25,31,19,10,5,55,39]
print(selection_sort(arr))