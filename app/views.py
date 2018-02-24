from flask import jsonify, render_template

from app import app
from models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_status')
def status():
    status = {
        'debug': app.config['DEBUG'],
        'database': app.config['SQLALCHEMY_DATABASE_URI'],
        # 'users': [user.username for user in User.query.all()],
    }
    return jsonify(status)


@app.route('/about')
def about():
    return render_template('about.html')


def create_account():
    return 'oh yeah'
