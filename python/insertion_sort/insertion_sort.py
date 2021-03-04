# PseudoCode:
#   InsertionSort(int[] arr)
  
#     FOR i = 1 to arr.length
    
#       int j <-- i - 1
#       int temp <-- arr[i]
      
#       WHILE j >= 0 AND temp < arr[j]
#         arr[j + 1] <-- arr[j]
#         j <-- j - 1
        
#       arr[j + 1] <-- temp


def insertion_sort(arr):
    for i in range(1, len(arr)):

        current = arr[i]
        where_we_are_in_arr = i
        while where_we_are_in_arr > 0 and arr[where_we_are_in_arr-1] > current:
            arr[where_we_are_in_arr] = arr[where_we_are_in_arr - 1]
            where_we_are_in_arr = where_we_are_in_arr - 1

        arr[where_we_are_in_arr] = current
        
    return arr
