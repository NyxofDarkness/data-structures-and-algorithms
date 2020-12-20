def binarySearch(arr, num):
    start = 0
    end = len(arr) - 1
    index = -1
    # (start, end) = (0, len(arr) - 1)

    while (start <= end) and (index == -1):
        mid = (start + end) // 2
        if arr[mid] == num:
            index = mid
        elif num < arr[mid]:
            end = mid -1
        else:
            start = mid + 1
    return index