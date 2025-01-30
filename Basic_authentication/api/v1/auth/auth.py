#!/usr/bin/env python3
"""module for API authentication management"""
from Flask import flask, request
from typing import List, TypeVar

User = TypeVar('User ')


class Auth:
    """class to manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """method to check if auth is required for a given path
        Args:
        path(str): the path to check
        excluded_paths(List[str]): a lis of paths that do not require auth

        returns:
        bool: false (auth logic to be implemented later)"""
        return False

    def authorization_header(self, request=None) -> str:
        """method to retrieve the authorization header from the request

        args:
        request: the flask request object

        returns:
        str: None (logic to be implemented later)"""
        return None

    def current_user(self, request=None) -> User:
        """method to retrieve the current user from the request
        args:
        request: the flask request object
        returns:
        User: None"""
        return None
