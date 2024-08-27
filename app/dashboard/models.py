from  ..auth.models import User
from  ..extensions import db


class SocialLinkModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    social_name = db.Column(db.String(255), nullable = False)
    social_username = db.Column(db.String(255), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))