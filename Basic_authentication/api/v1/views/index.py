#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1 import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> None:
    """GET /api/v1/unauthorized
    endpoint simulates an unauthorized access attempt.
    it raises a 401 unauthorized error, which is handled by the error handler
    """
    abort(401)


@app.views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> None:
    """GET /api/v1/forbidden
    endpoint simulates a forbidden access attempt.
    it raises a 403 forbidden error, which is handled by the error handler
    """
    abort(403)
