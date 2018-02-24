import os


env = os.environ

DEBUG = env.get('DEBUG', True)
SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = 8
