from flask import Flask, render_template



app = Flask(__name__)



@app.route('/basic')
def basic():

    return render_template('basic.html')

@app.route('/greet/<name>')
def greet(name):

    return render_template('greet.html', name=name)

@app.route('/Inventory')
def Inventroy():
    inventory_items = ['apple', 'orange', 'lime']
    return render_template('Inventory.html', inventory=inventory_items)
    
if __name__ == '__main__':

    app.run(debug=True)