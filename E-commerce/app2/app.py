from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

orders = []

@app.route('/')
def index():
    return render_template('order_form.html', orders=orders)

@app.route('/place_order', methods=['POST'])
def place_order():
    customer_name = request.form['customer_name']
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    orders.append({'customer_name': customer_name, 'product_name': product_name, 'quantity': quantity})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
