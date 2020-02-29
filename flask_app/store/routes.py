from store import app
from flask import render_template, url_for

items = {
    "apple": {
                "name": "apple"
            }
}


@app.route('/item/<name>')
def getInfo(name):
    return render_template("item.html", info=items[name]) if name in items else render_template("item.html", info={"name":"Unknown item"})

@app.route('/item')
def item():
    return render_template("item.html", info={"name":"Waiting for user input"})

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/')
def home():
    return render_template("index.html")
