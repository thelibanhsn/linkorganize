from flask import Blueprint, flash, url_for, render_template, redirect
from ..extensions import login_required, current_user
dashboard_bp = Blueprint('dashboard_bp', __name__, template_folder='templates')

@dashboard_bp.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
    # if not current_user.is_authenticated():
    #     return redirect(url_for('auth_bp/login'))
    return render_template('/dashboard.html')