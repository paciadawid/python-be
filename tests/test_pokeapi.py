import unittest

import requests
from faker import Faker
from hamcrest import *


class PokeAPITest(unittest.TestCase):
    base_url = "https://pokeapi.co/api/v2"

    pokemon_endpoint = "/pokemon"
    shape_endpoint = "/pokemon-shape"
    fake = Faker()

    def test_get_default_pokemons(self):
        response = requests.get(self.base_url + self.pokemon_endpoint)
        response_time = response.elapsed.microseconds / 1000
        response_body = response.json()
        assert_that(response_body, not_none())
        assert_that(response.status_code, equal_to(200))
        assert_that(response_body["count"], equal_to(1126))
        assert_that(response_time, less_than_or_equal_to(1000))

    def test_shape_name_vs_id(self):
        response_body = requests.get(self.base_url + self.shape_endpoint).json()
        assert_that(response_body["results"], has_length(response_body["count"]))
        shape_name = response_body["results"][2]["name"]
        response_body = requests.get(self.base_url + self.shape_endpoint + "/" + shape_name).json()
        assert_that(response_body["id"], equal_to(3))

    def test_random_pokemon_abilities(self):
        random_id = str(self.fake.random_int(1, 898))
        response_body = requests.get(self.base_url + self.pokemon_endpoint + "/" + random_id).json()
        name = response_body["name"]
        response_body = requests.get(self.base_url + self.pokemon_endpoint + "/" + name).json()
        assert_that(response_body["abilities"], not_(empty()))


if __name__ == '__main__':
    unittest.main()
