import unittest

from faker import Faker
from hamcrest import *

from config import TOKEN
from src.user_handler import UserHandler


class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.fake = Faker()
        self.user_handler = UserHandler(TOKEN)

    def test_create_user(self):
        user_data = self.user_handler.generate_unique_user_data()
        self.user_id = self.user_handler.create_user(user_data, 201)["id"]
        received_user_data = self.user_handler.get_user(self.user_id)
        assert_that(received_user_data, has_entries(user_data))

    def test_create_user_duplicate_email(self):
        user_data = self.user_handler.generate_unique_user_data()
        self.user_id = self.user_handler.create_user(user_data, 201)["id"]
        self.user_handler.create_user(user_data, 422)

    def test_create_user_malformed_email(self):
        user_data = self.user_handler.generate_unique_user_data()
        user_data["email"] = "test@"
        self.user_handler.create_user(user_data, 422)

    def test_delete_user(self):
        user_data = self.user_handler.generate_unique_user_data()
        self.user_id = self.user_handler.create_user(user_data)["id"]
        self.user_handler.delete_user(self.user_id, 204)
        response_body = self.user_handler.get_user(self.user_id, 404)
        assert_that(response_body["message"], equal_to("Resource not found"))

    def test_update_user(self):
        user_data = self.user_handler.generate_unique_user_data()
        self.user_id = self.user_handler.create_user(user_data)["id"]
        new_name = self.user_handler.generate_unique_user_data()["name"]
        self.user_handler.update_user(self.user_id, {"name": new_name})
        response_body = self.user_handler.get_user(self.user_id)
        assert_that(response_body, has_entry("name", new_name))

    def tearDown(self) -> None:
        if hasattr(self, "user_id"):
            self.user_handler.delete_user(self.user_id, False)


class PostsTests(unittest.TestCase):

    def test_post(self):
        pass


if __name__ == '__main__':
    unittest.main()
