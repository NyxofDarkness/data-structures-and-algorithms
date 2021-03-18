from hashtable.hashtable import HashTable

def test_create():
    hashtable = HashTable()
    assert hashtable

# Successfully hash a key to an in-range value
def test_hash_range():
    ht = HashTable()
    actual = ht._hash('vader')
    assert 0 <= actual < ht.size

def test_know_hash():
    ht = HashTable()
    first_run = ht._hash('Luke')
    second_run = ht._hash('Luke')
    assert first_run == second_run

def test_anagram():
    ht = HashTable()
    first_run = ht._hash('school master')
    second_run = ht._hash('the classroom')
    assert first_run == second_run

def test_anagram():
    ht = HashTable()
    first_run = ht._hash('school master')
    second_run = ht._hash('this should not work')
    assert first_run != second_run

def test_add_same():
    ht = HashTable()
    first_run = ht._hash('Luke')
    index = 451
    assert first_run == index

# Adding a key/value to your hashtable results in the value being in the data structure
def test_add():
    ht = HashTable()
    ht.add('milk', 'cookies')
    actual = ht.contains('milk')
    expected = True
    assert actual == expected

# Successfully handle a collision within the hashtable
# def test_add_same():
#     ht = HashTable()
#     ht.add('milk', 'cookies')
#     actual = ht.add('milk', 'cookies')
#     expected = 
#     assert actual == expected

# Retrieving based on a key returns the value stored
def test_get():
    ht = HashTable()
    ht.add('milk', 'coookies')
    actual = ht.get('milk')
    expected = 'coookies'
    assert actual == expected

# Successfully returns null for a key that does not exist in the hashtable
def test_contains():
    ht = HashTable()
    actual = ht.contains('milk')
    expected = False
    assert actual == expected
