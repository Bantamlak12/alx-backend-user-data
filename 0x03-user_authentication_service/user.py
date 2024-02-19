#!/usr/bin/env python3
"""
A module that implements a User Model
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """ Represents a use

    Attributes:
    - id (int): Unique identifier for the user.
    - email (str): The email address of the user.
    - hashed_password (str): The hashed password of the user.
    - session_id (str, optional): The session ID of the user.
    - reset_token(str, optional): The reset token for the user's password.
    """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
