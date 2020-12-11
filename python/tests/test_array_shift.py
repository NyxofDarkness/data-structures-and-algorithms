from array_shift.array_shift import array_length, insertShiftArray
 
# test = [3,4,5,6,7]
 
# def array_length(test):
#   return len(test)

def test_array_length():
    actual = array_length([3,4,5,6,7])
    expected = 5
    assert actual == expected

# def test_midpoint():
#   actual = midpoint( 2 % array_length(temp))
#   expected = 1
#   assert actual == expected

def test_insertion():
    actual = insertShiftArray([3,4,5,6,7], 2, 20)
    expected = [3,4,20, 5, 6, 7]
    assert actual == expected