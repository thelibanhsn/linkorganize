from ..extensions import db, UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False, unique=True)
    email = db.Column(db.String, nullable = False, unique=True)
    password = db.Column(db.String, nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
