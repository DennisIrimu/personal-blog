from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Role,Post
from .forms import CommentForm,PostForm
from . import main
from flask_login import login_required
from .. import db


@main.route('/')
def index():
    title = 'Home'
    posts = Post.get_posts()

    return render_template('index.html', title = title, posts=posts)
