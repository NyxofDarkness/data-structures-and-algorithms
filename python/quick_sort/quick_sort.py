def quick_sort(arr):
    left = []
    right = []
    equals = []

    if len(arr) <= 1:
        return arr
    if len(arr) > 1:
        pivot = arr[-1]

    for nums in arr:
        if nums < pivot:
            left.append(nums)
        elif nums == pivot:
            equals.append(nums)
        elif nums > pivot:
            right.append(nums)
    return quick_sort(left) + equals + quick_sort(right)

def partition(arr, left, right):
    pass

def swap(arr, i, low):
    pass