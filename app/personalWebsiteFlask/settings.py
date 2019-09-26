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

load_dotenv(d.joinpath('sec.env'))

ENV = getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL', default='sqlite:////tmp/test.db')
SECRET_KEY = getenv('SECRET_KEY', default='not-so-secret')
BCRYPT_LOG_ROUNDS = getenv('BCRYPT_LOG_ROUNDS', default=13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
