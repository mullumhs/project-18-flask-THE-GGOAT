from flask import Flask, render_template, url_for, request, redirect



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

@app.route('/profile/<username>')
def username(username):
    return render_template('profile.html', username=username)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you would typically save this data or send an email
        return redirect(url_for('thankyou', name=name, message=message))
    return render_template('contact.html')



@app.route('/thankyou')
def thankyou():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('thankyou.html', name=name, message=message)


    
if __name__ == '__main__':

    app.run(debug=True)