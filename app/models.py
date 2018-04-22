from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

class Role(db.Model):
    '''
    Define's a users role
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role', lazy='dynamic')

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(244))
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'
