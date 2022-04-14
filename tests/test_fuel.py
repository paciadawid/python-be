import unittest

from hamcrest import *

from basics.objective_basics import calculate_fuel


class FuelTest(unittest.TestCase):

    def test_12(self):
        assert_that(calculate_fuel(12), equal_to(2))

    def test_negative_value(self):
        assert_that(calculate_fuel(-1), equal_to(0))

    def test_1(self):
        assert_that(calculate_fuel(1), greater_than(0))

    def test_string(self):
        assert_that(calculate_fuel("test"), equal_to(False))


if __name__ == "__main__":
    unittest.main()
