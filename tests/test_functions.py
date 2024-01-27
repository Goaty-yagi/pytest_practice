import pytest

import source.functions as func

def test_add():
    result = func.add(5, 3)
    expected = 8

    assert result == expected

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