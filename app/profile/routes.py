from flask import Blueprint, render_template, redirect, url_for

profile_bp = Blueprint('profile_bp', __name__, template_folder='templates', url_prefix='/profile')

@profile_bp.route('/')
def profile():
    return 'PROFILE PAGE'