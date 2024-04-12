Basket Microservice:  
This is a simple Flask microservice for managing products in a basket.

Installation steps: 

Clone the repository:

git clone https://github.com/PRATHYUSHA0203/Morrisons_challenge_1.git


Navigate into the project directory:

cd Morrisons_challenge_1


Install dependencies using pip:

pip install -r requirements.txt


Usage

To run the Flask application:

python app.py


The server will start running locally.
The Endpoints and their functionality are as follows:

GET /

Returns a simple welcome message.

POST /products

Creates a new product. Send a JSON object in the request body with the following fields:

name: Name of the product which is a string value.

brand: Brand of the product which is a string value.

weight: Weight of the product which is an integer.

sku: Unique identifier for the product which is a string value.

available: Availability of the product a boolean value.

GET /products/<string:product_id>

Retrieves information about a specific product. Provide the product_id in the URL path.

DELETE /products/<string:product_id>

Deletes a product with the specified product_id.

PATCH /products/<string:product_id>

Updates information about a specific product. Provide the product_id in the URL path and send a JSON object with the fields to be updated in the request body.
