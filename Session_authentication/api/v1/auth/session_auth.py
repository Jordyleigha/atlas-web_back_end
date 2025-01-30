#!/usr/bin/env python3
""" User module
"""
from .auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ SessionAuth class
    """
    def __init__(self):
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """allows for multiple sessions per user ID,
        as it stores both the Session ID and user ID in the dictionary"""
        # returns none if user_id is None or not str
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        # generates a unique sess id using uuid.uuid4
        session_id = str(uuid.uuid4())
        # stores sess id and corressponding user id in the dict
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """retrieve the user ID associated with a given session ID"""
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        # returns the user_id if session_id is found in the dict
        user_id = self.user_id_by_session_id.get(session_id)
        # If user_id is not None it means the key was found in the dict
        # so it returns the user id
        return user_id if user_id is not None else None

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        user = User.get(user_id)
        return user
