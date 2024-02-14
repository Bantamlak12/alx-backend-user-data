#!/usr/bin/env python3
""" A module for view of session authentication
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth

            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            cookie_name = os.getenv('SESSION_NAME')
            response.set_cookie(cookie_name, session_id)
            return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ POST /auth_session/logout
    """
    from api.v1.app import auth

    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
