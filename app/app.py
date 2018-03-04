import pydash

from flask import Flask, jsonify, render_template, redirect, url_for, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import current_user, login_required


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/_status')
def status():
    status = {
        'debug': app.config['DEBUG'],
        'database': app.config['SQLALCHEMY_DATABASE_URI'],
        'logged_in_user': pydash.get(current_user, 'username'),
    }
    return jsonify(status)


@app.route('/about')
@login_required
def about():
    return render_template('about.html')


from routes import login
from routes import errors
