from flask.ext.login import login_user, logout_user, current_user, login_required

from flask import render_template, redirect, url_for, request, abort

from app.app import app
from app.helpers import is_safe_url
from app.forms import UsernamePasswordForm
from app.models import User, load_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if not user:
            return render_template('login.html', form=form, fail_message='no user by that depiction')

        if user.is_correct_password(form.password.data):
            login_user(user)
            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            return redirect(next or url_for('index'))
        else:
            return render_template('login.html', form=form, fail_message='incorrect password')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
