from hamcrest import *

from src.request_handler import RequestsHandler


class UserHandler(RequestsHandler):
    users_endpoint = "/users"

    def create_user(self, body: dict, expected_status_code=201):
        status_code, response_body = self.post_request(self.users_endpoint, body)
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def get_user(self, user_id, expected_status_code=200):
        status_code, response_body = self.get_request(self.users_endpoint + "/" + str(user_id))
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def delete_user(self, user_id, expected_status_code=204):
        status_code = self.delete_request(self.users_endpoint + "/" + str(user_id))
        if expected_status_code:
            assert_that(status_code, equal_to(expected_status_code))

    def update_user(self, user_id, body, expected_status_code=200):
        status_code, response_body = self.put_request(self.users_endpoint + "/" + str(user_id), body)
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def generate_unique_user_data(self):
        json_body = {
            "name": self.fake.name(),
            "gender": self.fake.random_element(elements=('male', 'female')),
            "email": self.fake.email(),
            "status": self.fake.random_element(elements=('active', 'inactive')),
        }
        return json_body
