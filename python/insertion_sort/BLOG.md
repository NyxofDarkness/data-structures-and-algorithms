# Writing Python Code To Sort By Insertion

> Sorting a list of elements using an insertion sorting algorithum, goes through your array one item at a time and sorts them for you by comparing the first index value you are working with, to the next in line. It's great for learning how to think through these problems, but less efficient on large arrays or lists.

## Let's go through the Solution!:

- The array we will be working with is: [8, 4, 23, 42, 16, 15]

- To start our code, we want to make a well named method, and take in our arr.
- Here we are telling the computer to take in the array, one index at a time, in order of the array. It takes a starting point of 1, and ends at the length of the array.
- This is the i!

``` python
def insertion_sort(arr):
    for i in range(1, len(arr)):
```

- The solution assumes [8] is a sorted list of the 1st item

``` python
     current = arr[i]
     where_we_are_in_arr = i

     while where_we_are_in_arr > 0 and arr[where_we_are_in_arr-1] > current:
         arr[where_we_are_in_arr] = arr[where_we_are_in_arr - 1]
         where_we_are_in_arr = where_we_are_in_arr - 1
```

- The solution checks [4] and finds it is greater than [8], so it shifts [8] to the right and inserts [4] in it's place.

- A shift looks like this: [ ][8]
- Now our array looks like [4][8]...

- The solution sets the current to [8]'s new position!

``` python
     arr[where_we_are_in_arr] = current
```

- Back in our loop, the solution checks [8] once again, but against it's new neighbor [23]

- [23] is found to be greater than [8], so the solution inserts [23] in that place

- Now our Array is: [4][8][23]

- Now the solution is checking [42]
- [42] is found to be greater than [8], so the solution inserts [42] in the end

- Now our Array is: [4][8][23][42]

- Now the solution checks [16]

- What's this? [16] isn't smaller than [42]!

- The solutionshifts it to the right

- The array now looks like this: [4][8][23][16][42]

- The solution checks again, and finds [16] is smaller than [23]

- So [16] is shifted to the right, giving us a new array of [4][8][16][23][42]

- That checks out right! So the last index in the array is now added and checked. [15]

- wash and repeat, the solution checks is against the index before it, until it no longer is bigger.

- finally we are presented with a sorted array: [4][8][15][16][23][42]

-Now we just return it so our tests can pass!

``` python
    return arr
```

## Ending Notes

It was a long road to get here! See what I mean by not efficient? It is great for learning how our code works, and for seeing what the calculations are actually doing. For small things, this is a great way of going about it. Since it is only checking the index before, this is able to work on all sorts of arrays! No matter the repeats, or order.

Thanks for coming to my insertion sort Ted Talk.
