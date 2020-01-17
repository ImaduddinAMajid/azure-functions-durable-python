import unittest
from azure.durable_functions.constants import (
    _DEFAULT_LOCAL_HOST,
    _DEFAULT_LOCAL_ORIGIN)


class TestConstants(unittest.TestCase):
    def test_default_local_host(self):
        self.assertEqual(_DEFAULT_LOCAL_HOST, "localhost:7071")

    def test_default_local_origin(self):
        self.assertEqual(_DEFAULT_LOCAL_ORIGIN, "http://localhost:7071")
