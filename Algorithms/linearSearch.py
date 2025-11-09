def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"Found {target} at {i}th index")
            break

arr = [5,18,20,1,55,23,31,90,65]
linear_search(arr,23)
        