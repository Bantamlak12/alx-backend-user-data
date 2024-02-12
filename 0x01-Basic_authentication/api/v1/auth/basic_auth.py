#!/usr/bin/env python3
""" Basic auth
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Base64 decoding
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_str = base64.b64decode(base64_authorization_header)
            if not decoded_str:
                return None
        except Exception as e:
            return
        return decoded_str.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ User credentials
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        user_credentials = decoded_base64_authorization_header.split(':')
        return (user_credentials[0], user_credentials[1])
