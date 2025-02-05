#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestMemoize(unittest.TestCase):
    """ test the memoize decorator """
    def test_memoize(self):
        """ test that memoize decorator stores result of function """
        class TestClass:
            """ class to test memoize decorator """
            def a_method(self):
                """ method to test memoize decorator """
                return 42

            @memoize
            def a_property(self):
                """ method to test memoize decorator """
                return self.a_method()
        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_method:
            instance = TestClass()
            result_1 = instance.a_property
            result_2 = instance.a_property
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)
            mock_method.assert_called_once()


class TestGetJson(unittest.TestCase):
    """test case for the get_json function
    contains unit tests to verify that the get_json function
    correctly retrieves JSON data from given URL"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("https://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """test the get_json function with mocked requests.get

        param test_url: the url to be passed to get_json
        param test_payload: expected JSON payload returned by the mock
        param mock_get: mocked requests.get method"""

        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


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
    def test_access_nested_map_exception(self, nested_map, path):
        """test that accessing a non-existent key raises a KeyError

        param nested_map: the nested dict to test
        param path: tuple represnting the path to the non-existent value
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

            self.assertEqual(str(context.exception), f"'{path[-1]}'")

    if __name__ == '__main__':
        unittest.main()
