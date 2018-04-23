from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    '''
    Define's a users role
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class User(UserMixin,db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(244))
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post',backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AtributeError('Password Attribute error')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'
    @classmethod
    def check_role(cls,user_id,role_id):
        get_role = User.query.filter_by(id=user_id).filter_by(role_id=role_id).first()
        return get_role

    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):

    __tablename__='posts'
    id=db.Column(db.Integer, primary_key = True)
    post_title=db.Column(db.String)
    post_content=db.Column(db.String)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='post', lazy='dynamic', )

    def save_post(self):
        db.session.add(self)
        db.session.commit()
