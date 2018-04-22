from . import db

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(244))
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'
