from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

@app.route('/')
def index():
    return render_template('product_form.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    products.append({'name': name, 'price': price})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
