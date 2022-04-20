import unittest

import requests
from hamcrest import *


class PunkAPITest(unittest.TestCase):
    base_url = "https://api.punkapi.com/v2/beers"

    def test_default_beers(self):
        response_body = requests.get(self.base_url).json()
        assert_that(response_body, has_length(25))
        assert_that(response_body[0]["id"], equal_to(1))

    def test_id_123(self):
        response_body = requests.get(self.base_url + "/123").json()
        assert_that(response_body, has_length(1))
        assert_that(response_body[0]["id"], equal_to(123))

    def test_80_elements_2nd_page(self):
        params = {
            "page": 3,
            "per_page": 50
        }
        first_id = params["per_page"] * (params["page"] - 1) + 1
        last_id = params["per_page"] * params["page"]
        response_body = requests.get(self.base_url, params=params).json()
        assert_that(response_body, has_length(params["per_page"]))
        assert_that(response_body[0]["id"], equal_to(first_id))
        assert_that(response_body[-1]["id"], equal_to(last_id))

    def test_ids_1_to_5(self):
        params = {
            "ids": "1|2|3|4|5"
        }
        response_body = requests.get(self.base_url, params=params).json()
        for i, beer in enumerate(response_body):
            assert_that(beer["id"], equal_to(i + 1))

    def test_abv_5_to_7(self):
        params = {
            "abv_gt": 4.9,
            "abv_lt": 7.1
        }
        response_body = requests.get(self.base_url, params=params).json()
        for beer in response_body:
            assert_that(beer["abv"], greater_than_or_equal_to(5))
            assert_that(beer["abv"], less_than_or_equal_to(7))

    def test_brewed_in_2010(self):
        params = {
            "brewed_before": "2011-01",
            "brewed_after": "2009-12"
        }
        response_body = requests.get(self.base_url, params=params).json()
        for beer in response_body:
            assert_that(beer["first_brewed"], ends_with("2010"))


if __name__ == '__main__':
    unittest.main()
