from store import app
from flask import render_template, url_for

items = {
    "apple" : {
                "name" : "apple"
            }
}


@app.route('/item/<name>')
def item(name):
    return render_template("index.html", info=items[name])
