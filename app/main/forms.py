from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PostForm(FlaskForm):
    post_title = StringField('Post Title')
    post_content = TextAreaField('Post Content')
    submit = SubmitField('Submit')
