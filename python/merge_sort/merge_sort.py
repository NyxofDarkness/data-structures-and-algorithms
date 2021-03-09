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
        