import os

env = os.environ

DEBUG = env.get('DEBUG', True)
SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URL', 'postgresql://localhost/speedcircuit')
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = 8
