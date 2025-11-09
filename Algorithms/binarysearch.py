# def binary_search(arr, target):
#     n = len(arr) 
#     low = 0
#     high = n - 1

#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return "value didn't exist"

# arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# print(binary_search(arr, 16))
# print(binary_search(arr,100))
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    mid = low + high // 2

    while low <= high:

        if arr[mid] == target:
            return mid
        elif arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

        return -1
        
arr = [1,3,5,7,9]
print(binary_search(arr, 6))



