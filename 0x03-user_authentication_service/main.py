#!/usr/bin/env python3
""" End-to-end integration test
"""
import requests


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"
URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """ Integeration test for user registration
    """
    data = {"email": email, "password": password}

    response = requests.post(f'{URL}/users', data=data)
    if response.status_code == 200:
        assert response.status_code == 200
        assert response.json() == {'email': email, 'message': 'user created'}

    if response.status_code == 400:
        assert response.json() == {'message': 'email already registered'}


def log_in_wrong_password(email: str, password: str) -> None:
    """ Integeration test for wrong password
    """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    if response.status_code == 401:
        assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Integeration test for user login
    """
    data = {"email": email, "password": password}
    response = requests.post(f'{URL}/sessions', data=data)
    if response.status_code == 200:
        assert response.json() == {'email': email, 'message': 'logged in'}
    elif response.status_code == 401:
        assert response.status_code == 401

    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """ Integeration test for profile unlogged.
    """
    response = requests.get(f'{URL}/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Integeration test for logged user
    """
    cookie = {"session_id": session_id}
    response = requests.get(f'{URL}/profile', cookies=cookie)
    if response.status_code == 200:
        assert response.status_code == 200
        assert response.json() == {'email': EMAIL}


def log_out(session_id: str) -> None:
    """ Integeration test for log out functionality
    """
    cookie = {"session_id": session_id}
    response = requests.delete(f'{URL}/sessions', cookies=cookie)
    if response.status_code == 200:
        assert response.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """ Integeration test for reset password token
    """
    response = requests.post(f'{URL}/reset_password', data={'email': email})
    if response.status_code == 200:
        reset_token = response.json()['reset_token']
        assert response.status_code == 200
        assert response.json() == {"email": email, "reset_token": reset_token}

    if response.status_code == 403:
        assert response.status_code == 403


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Integeration test for updating a password
    """
    data = {
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    }
    response = requests.put(f'{URL}/reset_password', data=data)
    if response.status_code == 200:
        assert response.status_code == 200
        message = {"email": email, "message": "Password updated"}
        assert response.json() == message

    if response.status_code == 403:
        assert response.status_code == 403


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
