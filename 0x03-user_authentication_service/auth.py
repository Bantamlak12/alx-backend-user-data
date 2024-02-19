#!/usr/bin/env python3
"""
A module that authenticate a user
"""
from sqlalchemy.orm.exc import NoResultFound
from user import User
from db import DB
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hash a password

    Args:
    - password (str): A password to be hashed

    Returns:
    - Bytes: A salted hash of the input password.
    """
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializes """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user

        Args:
        - email (str): The user email
        - password (str): The user password

        Returns:
        - A User object
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f'User {email} already exists')
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user
