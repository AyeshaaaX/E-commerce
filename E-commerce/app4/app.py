from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

customers = []

@app.route('/')
def index():
    return render_template('customer_form.html', customers=customers)

@app.route('/register_customer', methods=['POST'])
def register_customer():
    name = request.form['name']
    contact = request.form['contact']
    customers.append({'name': name, 'contact': contact})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
