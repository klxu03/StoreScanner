from store import app
from flask import render_template, url_for, session, request
from store.form import ItemForm
# Import sessions 
from flask_session import Session

items = {
    "apple": {
                "name": "apple"
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

@app.route('/')
def home():
    return render_template("index.html")
