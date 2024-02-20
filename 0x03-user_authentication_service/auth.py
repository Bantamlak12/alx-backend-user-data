#!/usr/bin/env python3
"""
A module that authenticate a user
"""
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
from db import DB
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """ Hash a password

    Args:
    - password (str): A password to be hashed

    Returns:
    - Bytes: A salted hash of the input password.
    """
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pwd


def _generate_uuid() -> str:
    """ Generate UUIDs

    Returns:
    - str: String representation of a new UUID
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """ Credentials validation

        Args:
        - email (str): The user email
        - password (str): The user password

        Returns:
        - bool
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Get session ID

        Args:
        - email (str): The user email

        Returns:
        - The session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ Find user by session ID

        Args:
        - session_is (str): User's session ID

        Returns:
        - Union[user, None]: User object or none
        """
        try:
            if session_id is None:
                return None
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroy session

        Args:
        - user_id (int): The user ID

        Returns:
        - None
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ Generate reset password token

        Args:
        - email (str): The user email

        Return:
        - str: The generated token
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                token = uuid.uuid4()
                user.reset_token = token
                return token
        except NoResultFound:
            raise ValueError
