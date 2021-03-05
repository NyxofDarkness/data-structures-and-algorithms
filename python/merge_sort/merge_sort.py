# ALGORITHM Mergesort(arr)
#     DECLARE n <-- arr.length
           
#     if n > 1
#       DECLARE mid <-- n/2
#       DECLARE left <-- arr[0...mid]
#       DECLARE right <-- arr[mid...n]
#       // sort the left side
#       Mergesort(left)
#       // sort the right side
#       Mergesort(right)
#       // merge the sorted left and right sides together
#       Merge(left, right, arr)

# ALGORITHM Merge(left, right, arr)
#     DECLARE i <-- 0
#     DECLARE j <-- 0
#     DECLARE k <-- 0

#     while i < left.length && j < right.length
#         if left[i] <= right[j]
#             arr[k] <-- left[i]
#             i <-- i + 1
#         else
#             arr[k] <-- right[j]
#             j <-- j + 1
            
#         k <-- k + 1

#     if i = left.length
#        set remaining entries in arr to remaining values in right
#     else
#        set remaining entries in arr to remaining values in len

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    i_left_index = 0
    j_right_index = 0
    k_result = []

    while i_left_index < len(left) and j_right_index < len(right):
        if left[i_left_index] < right[j_right_index]:
            k_result.append(left[i_left_index])
            i_left_index += 1
        else:
            k_result.append(right[j_right_index])
            j_right_index += 1

    k_result += left[i_left_index:]
    k_result += right[j_right_index:]
    return k_result


# def merge(left, right):
#     """Merge sort merging function."""

#     left_index, right_index = 0, 0
#     result = []
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1

#     result += left[left_index:]
#     result += right[right_index:]
#     return result


# def merge_sort(array):
#     """Merge sort algorithm implementation."""

#     if len(array) <= 1:  # base case
#         return array

#     # divide array in half and merge sort recursively
#     half = len(array) // 2
#     left = merge_sort(array[:half])
#     right = merge_sort(array[half:])

#     return merge(left, right)
        