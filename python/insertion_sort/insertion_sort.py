# PseudoCode:
#   InsertionSort(int[] arr)
  
#     FOR i = 1 to arr.length
    
#       int j <-- i - 1
#       int temp <-- arr[i]
      
#       WHILE j >= 0 AND temp < arr[j]
#         arr[j + 1] <-- arr[j]
#         j <-- j - 1
        
#       arr[j + 1] <-- temp

arr = [8,4,23,42,16,15]
def insertion_sort(arr):
    for i in range(len(arr)):
        # for each index on the length of the array, set to i
        min = i
        for j in range(i+1, len(arr)):
            #loop again, for each index, move forward to length of array
            if arr[min] > arr[j]:
                # if the i, or min index is greater than the next index at j, set min to j
                min = j
        # swap i and j index values, so the lowest is first
        arr[i], arr[min] = arr[min], arr[i]
    