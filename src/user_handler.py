from faker import Faker
from hamcrest import *

from src.request_handler import RequestsHandler


class UserHandler(RequestsHandler):
    users_endpoint = "/users"

    def create_user(self, body: dict, expected_status_code=201):
        status_code, response_body = self.post_request(self.users_endpoint, body)
        assert_that(status_code, equal_to(expected_status_code))
        return response_body["id"]

    def get_user(self, user_id, expected_status_code=200):
        status_code, response_body = self.get_request(self.users_endpoint + "/" + str(user_id))
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def delete_user(self, user_id, expected_status_code=204):
        status_code = self.delete_request(self.users_endpoint + "/" + str(user_id))
        assert_that(status_code, equal_to(expected_status_code))
        return status_code

    def generate_unique_user_data(self):
        fake = Faker()
        json_body = {
            "name": fake.name(),
            "gender": fake.random_element(elements=('male', 'female')),
            "email": fake.email(),
            "status": fake.random_element(elements=('active', 'inactive')),
        }
        return json_body
