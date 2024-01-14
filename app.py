from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session
from controller import *

app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def home():
    return render_template("index.html")


# TODO : NEW TEMPLATE
@app.route("/product", methods=["GET", "POST"])
def product():
    if request.method == "POST":
        name = request.form.get("name")
        brand = request.form.get("brand")
        price = request.form.get("price")

        status, data = ProductController.save(name, brand, price)

    return render_template("product_table.html", product_list=ProductController.find_all()[1])


@app.route("/product/<product_id>", methods=["DELETE"])
def remove_product(product_id):
    print("DELETE PRODUCT", product_id)
    ProductController.remove(product_id)
    return render_template("product_table.html", product_list=ProductController.find_all()[1])


@app.route("/customer", methods=['POST', 'GET'])
def customer():
    if request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        username = request.form.get("username")
        password = request.form.get('password')

        status, data = CustomerController.save(name, family, username, password)

    return render_template("customer_table.html", customer_list=CustomerController.find_all()[1])


@app.route('/customer/<customer_id>', methods=['DELETE'])
def remove_customer(customer_id):
    CustomerController.remove(customer_id)
    return jsonify({"status": "success"}), 200


@app.route("/store", methods=['POST', 'GET'])
def store():
    if request.method == "POST":
        name = request.form.get("name")
        brand = request.form.get("brand")
        price = request.form.get("price")
        quantity = request.form.get('quantity')

        status, data = CustomerController.save(name, brand, price, quantity)

    return render_template("store_table.html", store_list=StoreController.find_all()[1])


@app.route('/store/<store_id>', methods=['DELETE'])
def remove_store(store_id):
    StoreController.remove(store_id)
    return jsonify({"status": "success"}), 200


@app.route("/transaction", methods=['POST', 'GET'])
def transaction():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        product_id = request.form.get("product_id")
        quantity = request.form.get('quantity')
        customer = request.form.get('customer')
        product = request.form.get('product')

        status, data = CustomerController.save(customer_id, product_id, quantity, customer, product)

    return render_template("transaction_table.html", transaction_list=TransactionController.find_all()[1])


@app.route('/transaction/<transaction_id>', methods=['DELETE'])
def remove_transaction(transaction_id):
    TransactionController.remove(transaction_id)
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
