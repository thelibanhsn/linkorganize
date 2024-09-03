from flask import Blueprint, render_template, redirect, url_for
from ..extensions import current_user
home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))
    return render_template('/home.html')