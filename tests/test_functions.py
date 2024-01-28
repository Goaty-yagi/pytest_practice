import pytest

import source.functions as func

""" Function unit tests
    mark is for other developers. 
"""

@pytest.mark.skip(reason="This feature is currently broken")# This test will be skipped
def test_add():
    result = func.add(5, 3)
    expected = 8

    assert result == expected


def test_add_atrings():
    result = func.add("I love", " Python")
    expected = "I love Python"

    assert result == expected  # cause error


def test_divide():
    result = func.divide(12, 4)
    expected = 3

    assert result == expected


def test_divide_by_zero():
    # the following code causes error.
    # result = func.divide(30, 0)

    # test expected error occors.
    # You don't need assert.
    with pytest.raises(ZeroDivisionError):
        func.divide(30, 0)

@pytest.mark.xfail(reason="We know cannot divide by zero.")
def test_devide_zero_broken():
    func.divide(90, 0) 
