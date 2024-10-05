from flask import Blueprint, render_template, redirect, url_for, current_app, flash
from ..extensions import db, login_manager, login_required, current_user
from .forms import ProfileUpdateForm
from ..auth.models import User
from werkzeug.utils import secure_filename
import os
import uuid

profile_bp = Blueprint('profile_bp', __name__, template_folder='templates', url_prefix='/profile')

# All unauthorised return to login
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth_bp.login'))

@profile_bp.route('/')
@login_required
def profile():
 return render_template('/profile.html')

@profile_bp.route('/edit/<user_id>', methods = ['GET', 'POST'])
@login_required
def edit_profile(user_id):
 form = ProfileUpdateForm()
 user_info = User.query.filter_by(id=user_id).first()

 if form.validate_on_submit():
    if not user_info.username == form.username.data:
       is_username_exist = User.query.filter_by(username = form.username.data).first()
       if is_username_exist:
          flash('Username already exists', 'warning')
          return redirect(url_for('profile_bp.edit_profile', user_id=current_user.id))
    file = form.profile_pic.data
    if file:
        unique_filename = str(current_user.id )+ "_" + secure_filename(file.filename)

        upload_folder = os.path.join(current_app.root_path, 'static', 'assets', 'img', 'profiles')

        file.save(os.path.join(upload_folder, unique_filename))
        user_info.profile_pic = unique_filename

        # file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    user_info.first_name = form.first_name.data
    user_info.last_name = form.last_name.data
    user_info.user_title = form.user_title.data
    user_info.user_bio = form.user_bio.data
    user_info.email = form.email.data
    user_info.username = form.username.data


    db.session.commit()

    return redirect(url_for('profile_bp.profile'))
 return render_template('/update_profile.html', form=form, user_info=user_info)