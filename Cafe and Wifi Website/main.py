from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, URL, ValidationError
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[URL(message="Invalid URL"), DataRequired()])
    img_ulr = StringField('Image of the Cafe (URL)', validators=[URL(message="Invalid URL"), DataRequired()])
    location_name = StringField('Name of the Location', validators=[DataRequired()])
    power_outlet = BooleanField('Have Power Outlets ?', default=False, false_values=(False, 'false', 0, '0'))
    toilet = BooleanField('Have Toilet ?', default=False, false_values=(False, 'false', 0, '0'))
    wifi = BooleanField('Have WiFi ?', default=False, false_values=(False, 'false', 0, '0'))
    calls = BooleanField('Can take calls ?', default=False, false_values=(False, 'false', 0, '0'))
    seats = StringField('How many seats?', validators=[DataRequired()])
    coffee_price = StringField('Coffee Price in Pounds', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=['GET','POST'])
def add_new_place():
    form = CafeForm()
    success = False
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=request.form.get('cafe'),
            map_url=request.form.get('location'),
            img_url=request.form.get('img_ulr'),
            location=request.form.get('location_name'),
            seats=request.form.get('seats'),
            has_toilet=bool(request.form.get('toilet')),
            has_wifi=bool(request.form.get('wifi')),
            has_sockets=bool(request.form.get('power_outlet')),
            can_take_calls=bool(request.form.get('calls')),
            coffee_price=request.form.get('coffee_price')
        )
        db.session.add(new_cafe)
        db.session.commit()
        success = True

        return render_template("add.html", success=success)

    return render_template("add.html", form=form, success=success)


@app.route("/all")
def all():
    cafess = db.session.query(Cafe).all()
    cafesss = [cafe.to_dict() for cafe in cafess]
    return render_template("all.html", cafes=cafesss)


@app.route("/add")
def add():

    return render_template("add.html")


@app.route("/json")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


if __name__ == '__main__':
    app.run(debug=True)