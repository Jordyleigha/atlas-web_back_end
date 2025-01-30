#!/usr/bin/env python3
"""app module
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def flask_app():
    """initialize and configure flask application"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """registers a new user"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        if AUTH.register_user(email=email, password=password):
            response = {
                "email": email,
                "message": "user created"
            }
            return jsonify(response)
        else:
            raise ValueError("email already registered")
    except ValueError:
        response = {"message": "email already registered"}
        return jsonify(response), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """user login"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
        if not AUTH.valid_login(email=email, password=password):
            abort(401)
        session_id = AUTH.create_session(email=email)
        response = jsonify({
                "email": email,
                "message": "logged in",
        })
        response.set_cookie("session_id", session_id)
        return response
    except Exception:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """user logout"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """gets user profile"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """getting a reset password toekn"""
    try:
        email = request.form.get("email")
        reset_token = AUTH.get_reset_password_token(email)
        response = jsonify({"email": email, "reset_token": reset_token}), 200
        return response
    except Exception:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """update  the password"""
    try:
        email = request.form.get("email")
        reset_token = request.form.get("reset_token")
        new_password = request.form.get("new_password")
        AUTH.update_password(reset_token, new_password)
        response = {"email": email, "message": "Password updated"}
        return jsonify(response), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
