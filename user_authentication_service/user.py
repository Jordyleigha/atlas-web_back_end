#!/usr/bin/env python3
"""User model will create a database table named users
with the specified columns and constraints"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """The nullable=False parameter ensures that email and hashed_password
    cannot contain null values while session_id and reset_token
    can be null if not provided"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
