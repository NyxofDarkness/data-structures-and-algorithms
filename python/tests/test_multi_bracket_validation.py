import pytest
from multi_bracket_validation.multi_bracket_validation import multiBracketValidation

def insert():
    pass

def test_brackets_true():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_many():
    t = multi_bracket_validation('{}(){}')
    pass

# {}	TRUE
# {}(){}	TRUE
# ()[[Extra Characters]]	TRUE
# (){}[[]]	TRUE
# {}{Code}[Fellows](())	TRUE
# [({}]	FALSE
# (](	FALSE
# {(})	FALSE