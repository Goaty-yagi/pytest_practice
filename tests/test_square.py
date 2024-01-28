import pytest

from source.shapes import Square


""" parametrize test multiple times without loop."""


@pytest.mark.parametrize("side_length, expected_area", [[5, 25], (6, 36)])
def test_mutiple_square_areas(side_length, expected_area):
    assert Square(side_length).area() == expected_area


parameter = [[3, 12], (6, 24)]

@pytest.mark.parametrize("side_length, expected_perimeter", parameter)
def test_mutiple_perimeter(side_length, expected_perimeter):
    assert Square(side_length).perimeter() == expected_perimeter
