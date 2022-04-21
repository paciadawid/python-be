import unittest

from config import TOKEN
from faker import Faker
from hamcrest import *

from src.user_handler import UserHandler


class GoRESTTest(unittest.TestCase):

    def setUp(self) -> None:
        self.fake = Faker()
        self.user_handler = UserHandler(TOKEN)

    def test_create_user(self):
        user_data = self.user_handler.generate_unique_user_data()
        user_id = self.user_handler.create_user(user_data, 201)
        received_user_data = self.user_handler.get_user(user_id)
        assert_that(received_user_data, has_entries(user_data))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
