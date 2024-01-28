import math

import pytest

import source.shapes as shapes

# Prefix of the class should be test.
class TestCircle:

    def setup_method(self, method):
        """ a method named 'setup_method' run before test. """

        print(f"Setting up {method}") # print with -s flag
        self.circle = shapes.Circle(10) # Circle obj created

    def teardown_method(self, method):
        """ a method named 'teardown_method' run after test. """

        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
