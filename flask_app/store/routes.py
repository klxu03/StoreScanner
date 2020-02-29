from store import app
from flask import render_template, url_for

items = {
    "apple" : {
                "name" : "apple"
            }
}


@app.route('/item/<name>')
def getInfo(name):
    return render_template("index.html", info=items[name])

@app.route('/item')
def item():
    return render_template("item.html")

@app.route('/cart')
def cart():
    return render_template("item.html")