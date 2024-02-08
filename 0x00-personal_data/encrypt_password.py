#!/usr/bin/env python3
"""
Encrypts password and check for validity
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    parameter:
    - password: A password to be hashed

    Returns:
    - A salted, hashed password, which is a byte string
    """
    py_byte = password.encode()
    return bcrypt.hashpw(py_byte, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    parameters:
    - hashed_password (bytes): A hashed password
    - password (str): A password to check it with
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
