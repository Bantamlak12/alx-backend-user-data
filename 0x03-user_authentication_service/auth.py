#!/usr/bin/env python3
"""
A module that authenticate a user
"""
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
