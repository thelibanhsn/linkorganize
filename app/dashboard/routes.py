from flask import Blueprint, flash, url_for, render_template, redirect, request
from ..extensions import login_required, current_user,db,login_manager
from .forms import AddLinkForm, UpdateLinkForm, DeleteLinkForm
from .models import SocialLinkModel
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates' , url_prefix='/dashboard')

# All unauthorised return to login
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth_bp.login'))

@dashboard_bp.route('/', methods = ['GET', 'POST'])
@login_required
def dashboard():    
    social_links = SocialLinkModel.query.filter_by(user_id = current_user.id)

    return render_template('/dashboard.html', social_links=social_links)

@dashboard_bp.route('/add-social-link', methods=["GET", "POST"])
@login_required
def add_social():
    form = AddLinkForm()

    if form.validate_on_submit():
        data = SocialLinkModel(social_name = form.social_name.data.lower(), social_username = form.social_username.data.lower(), user_id=current_user.id)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    return render_template('/add_social.html', form=form)


@dashboard_bp.route('/edit-social-link/<social_link_id>', methods=["GET", "POST"])
@login_required
def update_social_link(social_link_id):
    form = UpdateLinkForm()
    social_link_data = SocialLinkModel.query.filter_by(id = social_link_id).first()

    if not social_link_data:
        # Handle case where social link with given ID does not exist
        flash('Social link not found.', 'error')
        return redirect(url_for('dashboard_bp.dashboard'))
    
    if form.validate_on_submit():
        social_link_data.social_name = form.social_name.data
        social_link_data.social_username = form.social_username.data
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    form.social_name.data = social_link_data.social_name
    form.social_username.data = social_link_data.social_username
    return render_template('/update_social.html', social_link_data=social_link_data, form=form)

@dashboard_bp.route('/delete-social-link/<social_link_id>', methods=["GET", "POST"])
@login_required
def delete_social_link(social_link_id):
    form = DeleteLinkForm()
    social_link_data = SocialLinkModel.query.filter_by(id = social_link_id).first()

    if not social_link_data:
        # Handle case where social link with given ID does not exist
        flash('Social link not found.', 'error')
        return redirect(url_for('dashboard_bp.dashboard'))
    
    if form.validate_on_submit():
        db.session.delete(social_link_data)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    
    form.social_name.data = social_link_data.social_name
    form.social_username.data = social_link_data.social_username
    return render_template('/delete_social.html', social_link_data=social_link_data, form=form)

