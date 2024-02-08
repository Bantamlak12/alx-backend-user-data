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
