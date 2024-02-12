#!/usr/bin/env python3
""" Module of authentication class
"""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """ Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if authentication is required for a given path while
            excluding certain paths.

        Parameters:
        - path (str): The path to check for authentication.
        - excluded_paths: List[str]: List of paths to exclude from
          authentication check.

        Returns:
        - bool: True if authentication is required, else False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Generate authentication header.

        Parameter:
        - request (optional): The HTTP Request for which the authorization
          header is generated. Default to None.

        Return:
        - str: The authorization header string
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user.

        Parameter:
        - request (optional): The http request from which to determine
          the current user. Defaults to None.

        Return:
        - TypeVar('User'): The current user object, ir None if not found.
        """
        return None
