from flask import abort, jsonify, redirect, render_template, request, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required

from food_mood import app, db_session, login_manager

from .models import User, Entry
from .forms import AddForm, LoginForm, SignupForm


@app.before_request
def before_request():
    g.user = current_user


# @app.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session.pop('_csrf_token', None)
#         if not token or token != request.form.get('_csrf_token'):
#             abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = 'flazeda'
    return session['_csrf_token']


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.jinja_env.globals['csrf_token'] = generate_csrf_token


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def home():
    return render_template('food_mood.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first_or_404()
        if user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        db_session.commit()
        login_user()
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
        eater = current_user

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


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
