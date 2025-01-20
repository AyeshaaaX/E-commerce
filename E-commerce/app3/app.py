from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

inventory = []

@app.route('/')
def index():
    return render_template('inventory_form.html', inventory=inventory)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    inventory.append({'product_name': product_name, 'quantity': quantity})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
