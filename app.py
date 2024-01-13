import os

from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session
from controller import *

app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/product", methods=['POST', 'DELETE', 'GET'])
def product():
    if request.method == "POST":
        name = request.form.get("name")
        brand = request.form.get("brand")
        price = request.form.get("price")

        status, data = ProductController.save(name, brand, price)
    elif request.method == "DELETE":
        ProductController.remove(request.args.get("id"))

        return render_template("product_table.html", product_list=ProductController.find_all())

    if request.method == "GET":
        return render_template("product_table.html", product_list=ProductController.find_all())


# @app.route('/remove/<product>')
# def remove(product):
#     return os.remove(product,product)
@app.route('/remove/<product_id>', methods=['DELETE'])
def remove(product_id):
    ProductController.remove(product_id)
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(debug=True)
