from store import app
from flask import render_template, url_for, session, request, redirect
from store.form import ItemForm
# Import sessions 
from flask_session import Session

items = {
    "apple": {
                "name": "apple"
            },
    "orange": {
                "name": "orange"
            }
}

# Create a session object and initilize it
sess = Session()
sess.init_app(app)


@app.route('/item/<name>')
def getInfo(name):
    return render_template("item.html", info=items[name]) if name in items else render_template("item.html", info={"name":"Unknown item"})

@app.route('/item', methods=['GET', 'POST'])
def item():
    itemForm = ItemForm()
    if itemForm.validate_on_submit():
        usrItem = request.form['item']
        print(usrItem)
        # go to the page of the given item
        return redirect(url_for('getInfo', name=usrItem))
    else:
    	return render_template("itemSearch.html", form=itemForm)

@app.route('/additem/<item>')
def additem(item):
    if session.get('items', False):
        session['items'].append(item)
    else:
        session['items'] = [item]
    return render_template("cart.html", items = session.get('items', []))

@app.route('/cart')
def cart():
    return render_template("cart.html", items = session.get('items', []))

@app.route('/scan')
def scan():
    return render_template("scan.html")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session['items'] = []
    return redirect(url_for("item"))