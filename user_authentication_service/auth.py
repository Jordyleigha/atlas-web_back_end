#!/usr/bin/env python3
"""auth module
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from user import User
from db import DB
import uuid


def _hash_password(password: str) -> bytes:
    """securley stores passwords"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """auth class to interact with authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register new user with email and password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """validate user login
        Tries to locates the user by email. If exists,
        check the password with bcrypt. If it matches return True.
        If other case, return False.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """The method should find the user by email, generate a new UUID for
        the session ID, store it in the database, and return the session ID."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = str(uuid.uuid4())
            self._db.update_user(user_id=user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """If session ID is None or no user is found,
        return None. Otherwise return the corresponding user"""
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """method updates the corresponding user’s session ID to None"""
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """find the user that corresponds to the email"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = str(uuid.uuid4())
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """find user corresponding to reset token"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password)
            self._db.update_user(user.id, reset_token=None)
        except NoResultFound:
            raise ValueError
