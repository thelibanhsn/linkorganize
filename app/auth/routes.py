from flask import Blueprint, flash, url_for, render_template, redirect
from .models import User
from ..extensions import db, login_user
from .forms import UserRegistrationForm, UserLoginForm
from werkzeug.security import generate_password_hash, check_password_hash
auth_bp = Blueprint('auth_bp', __name__,url_prefix='/auth',template_folder='templates')

@auth_bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data, username = form.username.data).first()
        if user:
            flash('User exists')
        else:
            hashed_password = generate_password_hash(form.password.data)
            data = User(first_name = form.first_name.data, last_name = form.last_name.data, username = form.username.data.lower(), email = form.email.data.lower(),password = hashed_password)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('auth_bp.login'))
    return render_template('/auth/register.html', form=form)

@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user and check_password_hash(user.password, form.password.data):
            flash('logged in successfully..')
            login_user(user)
            return redirect(url_for('home_bp.home'))
        else:
            flash('Email or Password are incorrect')
    return render_template('auth/login.html', form = form)

