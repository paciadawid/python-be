import unittest

from hamcrest import *

from basics.fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):

    def test_string(self):
        assert_that(fibonacci("test"), equal_to(False))

    def test_string_number(self):
        assert_that(fibonacci("5"), equal_to(3))

    def test_1st_element(self):
        assert_that(fibonacci(1), equal_to(0))

    def test_2st_element(self):
        assert_that(fibonacci(2), equal_to(1))

    def test_10st_element(self):
        assert_that(fibonacci(10), equal_to(34))



if __name__ == "__main__":
    unittest.main()
