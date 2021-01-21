import pytest
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def insert():
    pass

def test_brackets_true():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_many():
    actual = multi_bracket_validation('{}(){}')
    expected = True
    assert actual == expected

def test_extra_characters():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_a_lot():
    actual = multi_bracket_validation('(){}[[]]')
    expected = True
    assert actual == expected

def test_schoolshoutout():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def falsy_one():
    actual = multi_bracket_validation('[({}]')
    expected = False
    assert actual == expected

def falsy_two():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def falsy_three():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected

# [({}]	FALSE
# (](	FALSE
# {(})	FALSE