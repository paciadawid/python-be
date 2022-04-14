import unittest

from hamcrest import *

from basics.objective_basics import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_something(self):
        assert_that(self.calculator.add(1, 2), equal_to(3))

    def test_something2(self):
        assert_that(self.calculator.add(1, 2), equal_to(3))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
