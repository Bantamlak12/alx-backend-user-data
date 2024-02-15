#!/usr/bin/env python3
""" A module that manages session authentication with expiration feature.
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """
    Extends SessionAuth to manage session expiration.
    """

    def __init__(self):
        """ Initializes SessionAuth with session duration """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """ Creates and return session ID with current timestamp.

        Parameter:
        - user_id (str): ID of the user associated with the session

        Returns:
        - str: Session ID
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
            }
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Retrieves the user ID associated with a session ID.

        Parameter:
        - session_id (str): Session ID to look up.

        Returns:
        str: User ID if the session is valid and not expired. Otherwise None.
        """
        if session_id is None:
            return None

        if session_id not in self.user_id_by_session_id:
            return None

        session_info = self.user_id_by_session_id[session_id]

        if self.session_duration <= 0:
            return session_info.get('user_id')

        created_at = session_info.get('created_at')
        if not created_at:
            return None

        created_at_timestamp = created_at.timestamp()
        session_duration_timestamp = timedelta(
            seconds=self.session_duration).total_seconds()
        sum_timestamp = created_at_timestamp + session_duration_timestamp

        if datetime.now().timestamp() < sum_timestamp:
            return session_info.get('user_id')
        return None
