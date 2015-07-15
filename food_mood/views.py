import os
import logging

from flask import abort, redirect, render_template, request, url_for, g
from flask_wtf.csrf import CsrfProtect
from flask.ext.login import login_user, logout_user, current_user, login_required
from werkzeug import secure_filename

from food_mood import app, db_session, login_manager

from .models import User, Entry, UserProfile
from .forms import AddForm, LoginForm, SignupForm, PhotoForm

CsrfProtect(app)

logger = logging.getLogger(__name__)


@app.before_request
def before_request():
    g.user = current_user


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def home():
    if not current_user.is_anonymous():
        return render_template('food_mood.html', up=current_user.profile)
    return render_template('food_mood.html', up=None)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return redirect('/login')
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        db_session.commit()
        login_user(user)
        try:
            return redirect(url_for('home'))
        except:
            abort(500)
    return render_template('signup.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_food_mood():

    if request.method == 'POST':
        add_form = AddForm(request.form)
        if add_form.validate():
            entry = Entry(add_form.meal.data, add_form.food.data, add_form.mood.data, eater=current_user.get_id())
            db_session.add(entry)
            db_session.commit()
            return redirect('/')
        else:
            abort(500)
    else:
        add_form = AddForm()

    return render_template('add.html', form=add_form)


@app.route('/entries/<entry_id>/', methods=['GET'])
def entry(entry_id=None):
    if entry_id is not None:
        entry = Entry.query.get(entry_id)
        return render_template('entry.html', entry=entry, author=current_user.username)


# TODO: Fix this grossness of having two routes for the same endpoint
@app.route('/entries', methods=['GET'])
def entries():
        return render_template('entries.html', entries=Entry.query.filter_by(eater=current_user.id), author=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/users/profile_image', methods=['GET', 'POST'])
@login_required
def upload_file():
    form = PhotoForm()
    if request.method == 'POST':
        file = request.files[form.image.name]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            up = UserProfile(user=current_user.id)
            up.photo = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            db_session.add(up)
            db_session.commit()
            return redirect('/')
    return render_template('photo.html', form=form)

@app.route('/users/<user_id>/profile', methods=['GET'])
@login_required
def profile(user_id=None):
    user = User.query.get(user_id) or abort(404)
    return render_template('profile.html', user=user)
