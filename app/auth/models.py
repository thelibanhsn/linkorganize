from ..extensions import db, UserMixin
import uuid
from sqlalchemy.dialects.postgresql import UUID 
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String, nullable = False)
    user_title = db.Column(db.String(50), nullable=True)
    user_bio = db.Column(db.String(255), nullable=True)
    profile_pic = db.Column(db.String(255), nullable=True)
    otp = db.Column(db.String(255), nullable=True)
    qr_code = db.Column(db.LargeBinary, nullable=True)
    username = db.Column(db.String, nullable = False, unique=True)
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
