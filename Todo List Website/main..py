from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import CreateTodoForm, Users, LoginForm
from flask_gravatar import Gravatar
from functools import wraps
import re
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

ckeditor = CKEditor(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=True)
    task = relationship("Tasks", back_populates="author")


class Tasks(db.Model):
    __tablename__="user_tasks"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="task")
    title = db.Column(db.String(250), unique=True, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    task = db.Column(db.String(1000), nullable=False)


db.create_all()

gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Users()
    if form.validate_on_submit():

        if User.query.filter_by(email=form.email.data).first():
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('home'))

        hash_and_salted_password = generate_password_hash(
            form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            name=form.name.data,
            password=hash_and_salted_password,
            email=form.email.data
        )

        db.create_all()
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('tasks_list'))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("That email does not exist!")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Password is incorrect! ")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for("tasks_list"))
    return render_template("login.html", form=form)


@app.route("/list", methods=["GET", "POST"])
def add_new_list():
    form = CreateTodoForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        new_task = Tasks(
            title=form.title.data,
            date=form.date.data,
            task=form.body.data,
            author=current_user,
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("tasks_list"))
    return render_template("make-list.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/tasks')
def tasks_list():
    if not current_user.is_authenticated:
        flash("You need to login or register to see tasks.")
        return redirect(url_for("login"))
    tasks = Tasks.query.all()
    all_tasks = []
    for task in tasks:
        if task.author_id == current_user.id:
            stripped = re.sub('<[^<]+?>', '', task.task)
            task.task = stripped
            all_tasks.append(task)

    return render_template("index.html", all_tasks=all_tasks)


@app.route("/delete", methods=['POST'])
def delete_task():
    task_to_delete = request.form["task_to_delete"]
    print(task_to_delete)
    delete = Tasks.query.filter_by(title=request.form["task_to_delete"]).one()
    print(delete)
    db.session.delete(delete)
    db.session.commit()
    return redirect(url_for("tasks_list"))


if __name__ == '__main__':
    app.run(debug=True)