#!/usr/bin/env python3
""" A module that manages session authentication
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """ Manage session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a session ID for a user_id
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Returns a user ID based on a Session ID
        """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ Returns a user instance on a cookie value
        """
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ Deletes the user session / logout
        """
        if request is None:
            return False
        session_id_cookie = self.session_cookie(request)
        if not session_id_cookie:
            return False
        user_id = self.user_id_for_session_id(session_id_cookie)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id_cookie]

        return True
