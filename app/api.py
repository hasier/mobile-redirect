__author__ = 'hasier'

from flask import Response, request
from tropo import Session, Tropo

from app import app


@app.route('/')
def root():
    return Response(status=200)


@app.route('/tropo')
def tropo():
    session = Session(request.get_json(force=True))
    tropo = Tropo()
    tropo.say('It works!')
    return Response(response=tropo.RenderJson(), status=200, mimetype='application/json')