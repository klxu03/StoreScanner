from store import app
from flask import render_template, url_for

info = {
    "name" : "apple"
}

@app.route('/')
def home():
    return render_template("index.html", info = info)

@app.route('/item/<name>')
def item(name):
    info["name"] = name
    return render_template("index.html", info=info)