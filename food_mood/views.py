from flask import abort, redirect, render_template, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required

from food_mood import app, login_manager

from .models import User


@app.before_request
def before_request():
    g.user = current_user


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = 'flazeda'
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def home():
    return render_template('food_mood.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('/'))
    return render_template('login.html', title='Sign In')
