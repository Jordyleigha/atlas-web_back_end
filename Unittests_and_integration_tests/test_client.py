#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """ a test case class for testing GithubOrgClient
    class contains methods to the the org method
    of the GithubOrgClient
    it uses parameterized testing to verify the correct behaivor
    for different organization names
    """
    @parameterized.expand([
        ('google', {'name': 'Google LLC'}),
        ('abc', {'name': 'ABC Corp'})
    ])
    def test_org(self, org_name: str, expected_result: dict):
        """ tests the org method of GithubOrgClient

        arguments:
            org_name (str): name of organization to test
            expected_result (dict): expected result for given organization name
        """
        with patch.object(
            GithubOrgClient,
            'org',
            return_value=expected_result
        ):
            client = GithubOrgClient(org_name)
            result = client.org()
            self.assertEqual(result, expected_result)

    @parameterized.expand([
        ("test_org", "https://api.github.com/orgs/test_org/repos")
    ])
    def test_public_repos_url(self, org_name, expected_url):
        """ tests the _public_repos_url correctly returns
        the expected url based on org name provided"""

        mock_payload = {
            'repos_url': expected_url
        }
        """uses patch.object from unittest.mock lib
        to replace org propert with mock obj mock_org.
        the new_callable=PropertyMock arg specifies that the mock
        should be a property mock
        """
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = mock_payload
            client = GithubOrgClient(org_name)
            result = client._public_repos_url
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test public_repos method
        mock json response from githib api and tests that the
        public_repos method returns the expected list of repo names
        """
        mock_get_json.return_value = [
            {"id": 123456, "name": "repo1"},
            {"id": 789012, "name": "repo2"}
        ]
        expected_url = "https://api.github.com/orgs/test_org/repos"
        expected_repos = ["repo1", "repo2"]
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = expected_url
            client = GithubOrgClient("test_org")
            result = client.public_repos()
            self.assertEqual(result, expected_repos)
            mock_get_json.assert_called_once_with(expected_url)
            mock_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "match_license"}}, "match_license", True),
        ({"license": {"key": "no_match_license"}}, "match_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_returned_value):
        """tests the has_license method"""
        mock_get_json = patch('client.get_json').start()
        mock_get_json.return_value = repo
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = 'mock_url'
            client = GithubOrgClient('test_org')
            result = client.has_license(repo, license_key)
            self.assertEqual(result, expected_returned_value)
            patch.stopall()


if __name__ == '__main__':
    unittest.main()
