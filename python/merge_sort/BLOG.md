# Writing Python Code To Sort By Merging

> Sorting a list of elements using a merge sorting algorithum is based on spliting a list, into two comparably sized lists. They are each then sorted apart, then the two lists are merged together into one.

## Let's go through the Solution!:

## We start with the merge_sort method. This takes in an array as it's argument.

- First, we are just going to return the array if the length is less than or equal to 1. This way we know we have something to compare, and takes care of an edge case.

``` python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
```

- The array we will be working with is: [8, 4, 23, 42, 16, 15]

- Let's set some variables! 
- Mid is set to the length of the array divided by two. This gives us a midpoint! 

``` python
    mid = len(arr) // 2
```

> In this case, our mid point is 3.5

- Let's set left to the left side of our mid (that's what the : are for!) and use merge_sort on it- recursively!

``` python
 left = merge_sort(arr[:mid])
```

> left = [8, 4, 23]

- Let's do the same for right, but notice the : are on the other side of mid, so we get the correct side.

``` python
   right = merge_sort(arr[mid:])
```

> right = [42, 16, 15]

- Then we just do a return of our next method, merge! This takes our left and right lists, and merges them.

``` python
    return merge(left, right)
```

> The array is now [4, 8, 15, 16, 23, 42]   ... We did it!

### Let's go over the merge method!

- First, let's just set some variable. We will be keeping track of the left and right's index positions from  the merge_sort algo, and have an empty list ready to append our results into.

``` python
def merge(left, right):
    i_left_index = 0
    j_right_index = 0
    k_result = []
```

- We start with a while loop to iterate over the arrays. This will make sure the left and right indexes are not more than the length of the left and right arrays from the merge_sort algorithum.

-reminder of our left/right

``` python
left = [8, 4, 23]
right = [42, 16, 15]
```

``` python
    while i_left_index < len(left) and j_right_index < len(right):
```

- Next we will compare the left and right values at the same indexes. If the left is less than the right it is appended to our k_result, and moves the index up one.

``` python
        if left[i_left_index] < right[j_right_index]:
            k_result.append(left[i_left_index])
            i_left_index += 1
```

- Otherwise, It appends the right into our k_result, since it would be bigger! Also it moves us up an index.

``` python
        else:
            k_result.append(right[j_right_index])
            j_right_index += 1
```

Now all we have to do is take that k_result list, and simutaniously set it equal to, and add to the left and right results. 

``` python
    k_result += left[i_left_index:]
    k_result += right[j_right_index:]
```

- Now just return k_result, because we returned the new list in the merge_sort method. 

``` python
    return k_result
```

Thank you for coming to my merge_sort Ted Talk. Hopefully this cleared some stuff up. personally I found it rather confusing to have my array being split up and going between the two methods, but I understand this would be an easy thing for a computational device. noice.