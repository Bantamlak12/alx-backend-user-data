#!/usr/bin/env python3
""" Basic auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Implements Basic auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Base64 encodeding
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]
