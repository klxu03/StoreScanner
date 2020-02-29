from store import app
from flask import render_template, url_for

items = {
    "apple": {
                "name": "apple"
            }
}


@app.route('/item/<name>')
def item(name):
	if name not in items: # this item is not in the list of available items
		itemInfo = {"name": "undefined"}
	else:
		itemInfo = items[name]
	return render_template("index.html", info=itemInfo)
