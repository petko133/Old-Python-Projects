from PIL import Image, ImageColor
from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory
from flask_bootstrap import Bootstrap
from io import BytesIO
import requests
import os

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Bootstrap(app)


@app.route("/", methods=["POST", "GET"])
def home():
    url = "https://pe-images.s3.amazonaws.com/photo-editing/cc/unify-colors/color-shapes.png"
    response = requests.get(url)
    hexes = get_hex(response)
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            hexes = get_hex(image)
            return render_template("index.html", hexes=len(hexes), url=url, filename=filename, hex_code=hexes)

    return render_template("index.html", hexes=len(hexes), url=url, hex_code=hexes)


@app.route("/image/<filename>", methods=["POST", "GET"])
def static_img(filename):
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = image.filename
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def get_hex(response):
    dictc = {}
    try:
        im = Image.open(BytesIO(response.content)).convert('RGB')
    except AttributeError:
        im = Image.open(response).convert('RGB')

    for i in range(im.width):
        for j in range(im.height):
            h = im.getpixel((i, j))
            if h in dictc:
                dictc[h] = dictc[h] + 1
            else:
                dictc[h] = 1
    # sort by values rather than keys descending
    a = sorted(dictc.items(), key=lambda x: x[1], reverse=True)
    colour_sort = []
    hex_sort = []
    for n in range(10):
        colour_sort.append(a[n][0])

        hex_sort.append(rgb2hex(colour_sort[n][0], colour_sort[n][1], colour_sort[n][2]))

    return hex_sort


if __name__ == '__main__':
    app.run(debug=True)
