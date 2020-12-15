def binarySearch(arr, num):
    mid = 0
    start = 0
    end = len(arr)
    step = 0

    while (start <= end):
        step = step + 1
        mid = (start + end) // 2

        if num == arr[mid]:
            return mid

        if num < arr[mid]:
            end = mid -1

        else:
            start = mid + 1
    return -1