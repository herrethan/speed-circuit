import os

env = os.environ

DEBUG = env.get('DEBUG', True)
ENVIRONMENT = env.get('ENVIRONMENT', 'development')
SECRET_KEY = env.get('SECRET_KEY', 'speedy')

SQLALCHEMY_DATABASE_URI = env.get('DATABASE_URL', 'postgresql://localhost/speedcircuit')
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = 8
