from array_binary_search.array_binary_search import binarySearch

def test_works():
    actual: binarySearch([4,8,15,16,23,42], 15)
    expected: 2
    assert actual == expected

def test_works2():
    actual: binarySearch([11,22,33,44,55,66,77], 90)
    expected: -1
    assert actual == expected