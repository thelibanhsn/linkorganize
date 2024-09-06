from flask import Blueprint, render_template, redirect, url_for
from ..dashboard.models import SocialLinkModel
from ..auth.models import User
from ..extensions import current_user

social_links_bp = Blueprint('social_links_bp', __name__, template_folder='templates')

@social_links_bp.route('/<username>')
def social_links(username):
    links = SocialLinkModel.query.filter_by(user_id = current_user.id).all()
    return render_template('/index.html', links = links)