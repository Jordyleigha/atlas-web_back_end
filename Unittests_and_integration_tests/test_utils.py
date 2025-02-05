#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """class contains a unittest to verify access_nested_map function
    correctly retreives values from the nested dict based on specific paths"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
        """ test the access_nested_map function with various inputs

        param nested_map: the nested dict to test
        param path: a tuple representing the path to desired value
        param expected: expected result for the given input
        """

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_acess_nested_map_exception(self, nested_map, path):
        """test that accessing a non-existent key raises a KeyError

        param nested_map: the nested dict to test
        param path: tuple represnting the path to the non-existent value
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

            self.assertEqual(str(context.exception), f"'{path[-1]}'")

    if __name__ == '__main__':
        unittest.main()
