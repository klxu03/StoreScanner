import os
from store import app
from flask import render_template, url_for, session, request, redirect
from store.form import ItemForm, ListForm
# Import sessions
from flask_session import Session
from werkzeug.utils import secure_filename

items = {
    "apple": {
                "name": "apple",
                "price": 1.99
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
        itemText = request.form['item']
        itemImage = request.form['picture']
        if itemText is not "": # there's something in the text form
            print(itemText)
            # go to the page of the given item
            return redirect(url_for('getInfo', name=itemText))
        else: # no text - is there a picture? (TODO)
            print("No text!")
            print(itemImage)
            return redirect(url_for('getInfo', name='apple')) #temporarily just redirect to /items/apple
    else:
    	return render_template("itemSearch.html", form=itemForm)

@app.route('/additem/<item>')
def additem(item):
    if session.get('items', False):
        if session.get('counts', False):
            if item in session['counts']:
                session['counts'][item] += 1
            else:
                session['counts'][item] = 1
        else:
            session['counts'][item] = 1
    else:
        session['items'] = [item]
        session['counts'][item] = 1
    return redirect(url_for("cart", items = session.get('items', [])))

@app.route('/cart')
def cart():
    return render_template("cart.html", items = session.get('items', []))

@app.route('/shoppinglist')
def shoppinglist():
    listForm = ListForm()
    if listForm.validate_on_submit():
        listItem = request.form['item']
        print(listItem)
    return render_template("shoppinglist.html", form=listForm, shoppinglist = session.get('shoppinglist', []))

@app.route('/addlistitem', methods=['POST'])
def addlistitem():
    if session.get('shoppinglist', False):
        session['shoppinglist'].append()
    return render_template("shoppinglist.html", shoppinglist = session.get('shoppinglist', []))

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':            
            photo.save(os.path.join('./store/image-upload', photo.filename))
    return redirect(url_for('fileFrontPage'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/logout')
def logout():
    session['items'] = []
    return redirect(url_for("item"))
