from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreateTodoForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    date = DateField('Date', validators=[])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit List")

class Users(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name")
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

