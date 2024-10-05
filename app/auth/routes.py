from flask import Blueprint, flash, url_for, render_template, redirect, request
from .models import User
from ..extensions import db, login_user, logout_user, current_user, mail
from .forms import UserRegistrationForm, UserLoginForm, ForgetPasswordForm, OtpForm, ResetPasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
import random
from flask_mail import Message

auth_bp = Blueprint('auth_bp', __name__,url_prefix='/auth',template_folder='templates')

# user register view
@auth_bp.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data, username = form.username.data).first()
        if user:
            flash('User exists', 'warning')
        else:
            hashed_password = generate_password_hash(form.password.data)
            data = User(first_name = form.first_name.data, last_name = form.last_name.data, username = form.username.data.lower(), email = form.email.data.lower(),password = hashed_password)
            db.session.add(data)
            db.session.commit()
            login_user(data)
            return redirect(url_for('profile_bp.edit_profile', user_id=current_user.id))
    return render_template('/auth/register.html', form=form)

# login view
@auth_bp.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))

    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data.lower()).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard_bp.dashboard'))
        else:
            flash('Email or Password are incorrect', 'danger')
    return render_template('auth/login.html', form = form)

# logout view
@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))


# generate otp view
@auth_bp.route('/forget-password', methods=['GET', 'POST'])
def forget_password():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))
    
    form = ForgetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        
        if user:
            otp = random.randint(100000, 999999)
            print('otp:', otp)
            user.otp=otp
            db.session.commit()

            send_otp_email(user.email, otp)
            flash('OTP has been sent to your email', 'info')
            return redirect(url_for('auth_bp.verify_otp',email=user.email))
        else:
            flash('No account with that email', 'warning')
    return render_template('auth/forget_password.html', form=form)

# Send OTP Email Function
def send_otp_email(email, otp):
    msg = Message('Your OTP', recipients=[email])
    msg.body = f'Your OTP is {otp}'
    mail.send(msg)

# OTP verification view
@auth_bp.route('verify-otp', methods=['GET', 'POST'])
def verify_otp():
    form = OtpForm()
    email = request.args.get('email')
    print('Email received in verify-otp route:', email)
    
    user = User.query.filter_by(email=email).first()
    
    if form.validate_on_submit():
        
        if str(user.otp) == form.otp.data:
            flash('OTP verified. You can now reset your password.', 'success')
            return redirect(url_for('auth_bp.reset_password', email=user.email))
        else:
            flash('Invalid OTP', 'danger')
    return render_template('auth/verify_otp.html', form=form)

# reset password view
@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    
    email = request.args.get('email')
    print('Email received in verify-otp route:', email)

    user = User.query.filter_by(email=email).first()
    
    if form.validate_on_submit():
        user.password = generate_password_hash(form.password.data)
        user.otp = None
        db.session.commit()
        flash('Your password has been updated!', 'success')
        return redirect(url_for('auth_bp.login'))
    
    return render_template('auth/reset_password.html', form=form)