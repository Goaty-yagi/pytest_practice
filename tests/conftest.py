import pytest

from source.shapes import Rectangle
""" conftest.py will be parsed by pytest, and fixture functions
will be globalized within the scope.

"""


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 30)


@pytest.fixture
def other_rectangle():
    return Rectangle(4, 5)
