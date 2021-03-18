import pytest
from repeated_word.repeated_word import Repeats

def test_find_repeat():
    string_input = 'Once upon a time, there was a brave princess who...'
    testing = Repeats()
    actual = testing.find_repeated_words(string_input)
    expected = 'a'
    assert actual == expected

def test_capitals():
    string_input = 'Here I go, Hello world! Go do something awesome!'
    testing = Repeats()
    actual = testing.find_repeated_words(string_input)
    expected = 'go'
    assert actual == expected

def test_repeats_method():
    assert Repeats()

def test_no_unique():
    string_input = 'Hello, I am a string of no repeating words!'
    testing = Repeats()
    actual = testing.find_repeated_words(string_input)
    expected = "String is Unique ['hello,', 'i', 'am', 'a', 'string', 'of', 'no', 'repeating', 'words!']"
    assert actual == expected