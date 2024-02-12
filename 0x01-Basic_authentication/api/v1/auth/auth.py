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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            if path == excluded_paths or path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Generate authentication header.

        Parameter:
        - request (optional): The HTTP Request for which the authorization
          header is generated. Default to None.

        Return:
        - str: The authorization header string
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user.

        Parameter:
        - request (optional): The http request from which to determine
          the current user. Defaults to None.

        Return:
        - TypeVar('User'): The current user object, ir None if not found.
        """
        return None
