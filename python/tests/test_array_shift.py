from array_shift.array_shift import insertShiftArray

def test_insertion_even():
    actual = insertShiftArray([3,4, 5,6,7], 20)
    expected = [3,4, 5, 20, 6, 7]
    assert actual == expected

def test_insertion_odd():
    actual = insertShiftArray([3, 4, 5, 6, 7, 8], 20)
    expected = [3, 4, 5, 20, 6, 7, 8]
    assert actual == expected

