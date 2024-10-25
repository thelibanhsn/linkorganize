from flask import Blueprint, render_template, redirect, url_for, request
from ..dashboard.models import SocialLinkModel
from ..auth.models import User
from ..extensions import current_user

social_links_bp = Blueprint('social_links_bp', __name__, template_folder='templates')

@social_links_bp.route('/<username>')
def social_links(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template('/not_found.html')
    links = SocialLinkModel.query.filter_by(user_id = user.id).all()
    return render_template('/index.html', links = links, user = user)
    
