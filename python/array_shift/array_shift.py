# test = [3,4,5,6,7]
# insert_value = 20
# index = 2

def insertShiftArray(arr, num):
    array_length = len(arr)

    if array_length%2:
        middle_of_array = round(array_length // 2) + 1
    else:
        middle_of_array = array_length // 2
    arr.insert(middle_of_array, num)

    return arr

