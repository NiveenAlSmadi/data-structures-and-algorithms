from multi_bracket_validation import __version__
from multi_bracket_validation.multi_bracket_validation import  multi_bracket_validation

def test_version():
    assert __version__ == '0.1.0'


def test_1():
    expected=True
    actual= multi_bracket_validation("{}")
    assert expected==actual

def test_2():
    expected=True
    actual= multi_bracket_validation("{}(){}")
    assert expected==actual

def test_3():
    expected=True
    actual= multi_bracket_validation("()[[Extra Characters]]")
    assert expected==actual

def test_4():
    expected=True
    actual= multi_bracket_validation("(){}[[]]")
    assert expected==actual    

def test_5():
    actual = multi_bracket_validation("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected

def test_6():
    actual = multi_bracket_validation("[({}]")
    expected = False
    assert actual == expected

def test_7():
    actual = multi_bracket_validation("(](")
    expected = False
    assert actual == expected


def test_8():
    actual = multi_bracket_validation("{(})")
    expected = False
    assert actual == expected


def test_9():
    actual = multi_bracket_validation("{")
    expected = False
    assert actual == expected


def test_10():
    actual = multi_bracket_validation("]")
    expected = False
    assert actual == expected 


    