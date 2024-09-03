from  ..auth.models import User
from  ..extensions import db, current_user


class SocialLinkModel(db.Model):
    __tablename__ = 'social_links'
    id = db.Column(db.Integer, primary_key=True, )
    social_name = db.Column(db.String(255), nullable = False)
    social_username = db.Column(db.String(255), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))