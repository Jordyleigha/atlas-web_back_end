#!/usr/bin/env python3
"""Authentication class responsible for handling authentication logic"""
from flask import request
from typing import List, TypeVar


class Auth:
    """class that has methods to check authentication requirements,
    authorization headers, and identitfy the current user
    """

    def __init__(self):
        """Initialize the Auth object"""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for path"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Extract the authorization header from request"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """Get the current authenticated user"""
        return None
