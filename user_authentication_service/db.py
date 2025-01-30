#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """add new user"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return self._session.query(User).filter_by(email=email).first()

    def find_user_by(self, **kwargs) -> User:
        """find a user by various info"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if user is None:
                raise NoResultFound
            return user
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the user's attributes based on the provided keyword args"""
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise ValueError
            self._session.commit()
        except NoResultFound:
            raise NoResultFound
        except InvalidRequestError:
            raise InvalidRequestError
