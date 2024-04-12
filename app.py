from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Basket Microservice'


products = []


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json

    name = data.get('name')
    brand = data.get('brand')
    weight = data.get('weight')
    sku = data.get('sku')
    available = data.get('available')

    for product in products:
        if product['sku'] == sku:
            return jsonify({"sku": sku,
                            "message": f"product {sku} already exists"}), 409

    new_product = {
        'name': name,
        'brand': brand,
        'weight': weight,
        'sku': sku,
        'available': available
    }

    products.append(new_product)

    return jsonify({"sku": sku,
                    "message": f"product {sku} created"}), 201


@app.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['sku'] == product_id), None)
    if product:
        return jsonify(product), 200
    else:
        return ('',404)
        #return jsonify({"message": f"Product with SKU {product_id} does not exist"}), 404


@app.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product_exists = any(product['sku'] == product_id for product in products)
    if product_exists:
        products = [product for product in products if product['sku'] != product_id]
        return ('',200)
        #return jsonify({"message": f"Product with SKU {product_id} deleted"}), 200

    else:
        return ('',404)
        #return jsonify({"message": f"Product with SKU {product_id} does not exist"}), 404


@app.route('/products/<string:product_id>', methods=['PATCH'])
def update_product(product_id):
    data = request.json
    product = next((product for product in products if product['sku'] == product_id), None)
    if product:
        product.update(data)
        return jsonify({"sku": product_id, "message": f"product {product_id} updated"}), 200
    else:
        return ('',404)
        #return jsonify({"message": f"Product with SKU {product_id} does not exist"}), 404


if __name__ == '__main__':
    app.run(debug=True)
