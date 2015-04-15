__author__ = 'hasier'

from flask import Response, jsonify, request
from tropo import Session

from app import app


@app.route('/')
def root():
    return Response(status=200)


@app.route('/tropo')
def tropo():
    session = Session(request.get_json(force=True))
    return jsonify({
        "tropo": [{"say": {"value": "It works!"}}]
    })