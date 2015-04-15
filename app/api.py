__author__ = 'hasier'

from flask import Response

from app import app


@app.route('/')
def root():
    return Response(status=200)