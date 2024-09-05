from flask import Blueprint, render_template, redirect, url_for
from ..extensions import db, login_manager, login_required, current_user
from .forms import ProfileUpdateForm
from ..auth.models import User
profile_bp = Blueprint('profile_bp', __name__, template_folder='templates', url_prefix='/profile')

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
  user_info.first_name = form.first_name.data
  user_info.last_name = form.last_name.data
  user_info.user_title = form.user_title.data
  user_info.user_bio = form.user_bio.data
  user_info.email = form.email.data
  user_info.username = form.username.data

  db.session.commit()

  return redirect(url_for('profile_bp.profile'))
 return render_template('/update_profile.html', form=form, user_info=user_info)