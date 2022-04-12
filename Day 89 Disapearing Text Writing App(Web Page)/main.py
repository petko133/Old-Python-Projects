from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
Bootstrap(app)


@app.route("/")
def home():

    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
