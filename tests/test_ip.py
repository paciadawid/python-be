import unittest

import requests
from hamcrest import *


class IPTest(unittest.TestCase):
    def test_if_ip_exists(self):
        params = {"format": "json"}
        response_body = requests.get("https://api.ipify.org/", params=params).json()
        assert_that(response_body, has_key("ip"))
        assert_that(response_body["ip"], matches_regexp("([0-9]{1,3}\.){3}[0-9]{1,3}$"))


if __name__ == '__main__':
    unittest.main()
