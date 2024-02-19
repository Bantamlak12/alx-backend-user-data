#!/usr/bin/env python3
"""
A flask App
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def get():
    """ Return a simple JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def post():
    """ Register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        new_user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")