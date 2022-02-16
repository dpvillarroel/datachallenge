from flask import Flask, jsonify, abort, render_template
import products_controller
from productsDB import write_db

app = Flask(__name__)

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route("/", methods=["GET"])
def get_products():
    all_products= products_controller.get_products()
    return render_template('products.html', products=all_products)
  

# Part 2
@app.route("/product/<id>", methods=["GET"])
def get_product_by_id(id):
    average = products_controller.get_by_id(id)
    if average is None:
        abort(404, description="Resource not found")

    return jsonify(average)

if __name__ == "__main__":
    #Part 1
    write_db()
    app.run(host='0.0.0.0', port=8000, debug=True)