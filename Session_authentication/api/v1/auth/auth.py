#!/usr/bin/env python3
"""Authentication class responsible for handling authentication logic"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """class that has methods to check authentication requirements,
    authorization headers, and identitfy the current user
    """

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
        Authorization = request.headers.get("Authorization")
        if request is not None:
            return Authorization
        else:
            return None

    def current_user(self, request=None) -> TypeVar("User"):
        """Get the current authenticated user"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        # retrieves session name fro env vars
        # os.environ.get used to safely retrieve env vars
        # if session name is not set default to _my_session_id
        session_name = getenv('SESSION_NAME')
        # retireve cookie val associated with session name
        return request.cookies.get(session_name)
