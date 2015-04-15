__author__ = 'hasier'

from flask import Flask
from redis.utils import from_url

from config import REDIS_URL

app = Flask(__name__)
app.config.from_object('app.config')
redis = from_url(REDIS_URL)

import api