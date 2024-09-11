from  ..auth.models import User
from  ..extensions import db, current_user
from sqlalchemy.dialects.postgresql import UUID 
import uuid

class SocialLinkModel(db.Model):
    __tablename__ = 'social_links'
    id = db.Column(db.Integer, primary_key=True, )
    social_name = db.Column(db.String(255), nullable = False)
    social_username = db.Column(db.String(255), nullable = False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='social_links', lazy=True)
