from hamcrest import *

from src.request_handler import RequestsHandler
from src.user_handler import UserHandler


class PostHandler(RequestsHandler):
    posts_endpoint = "/posts"

    def create_post(self, user_id, body, expected_status_code=201):
        status_code, response_body = self.post_request(UserHandler.users_endpoint + f"/{user_id}" + self.posts_endpoint,
                                                       body)
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def get_post(self, post_id, expected_status_code=200):
        status_code, response_body = self.get_request(self.posts_endpoint + f"/{post_id}")
        assert_that(status_code, equal_to(expected_status_code))
        return response_body

    def generate_post_content(self):
        post_body = {
            "title": self.fake.sentence(nb_words=10),
            "body": self.fake.paragraph(nb_sentences=5)
        }
        return post_body
