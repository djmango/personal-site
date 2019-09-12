# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""

from os import getenv
from pathlib import Path  # python3 only

from dotenv import load_dotenv

# `path.parents[1]` is the same as `path.parent.parent`
d = Path(__file__).resolve().parents[1]

load_dotenv(d.joinpath('pub.env'))
load_dotenv(d.joinpath('sec.env'))


ENV = getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
if getenv('SECRET_KEY') is None:
    SECRET_KEY = 'not-so-secret'  # only for CI build NOT PROD
else:
    SECRET_KEY = getenv('SECRET_KEY')
BCRYPT_LOG_ROUNDS = getenv('BCRYPT_LOG_ROUNDS', default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = d.joinpath('static', 'build', 'manifest.json')