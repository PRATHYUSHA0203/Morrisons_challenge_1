import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_product(client):
    
    data = {
        "name": "Product 1",
        "brand": "Brand 1",
        "weight": 10,
        "sku": "12345",
        "available": True
    }
    response = client.post('/products', json=data)
    assert response.status_code == 201
    assert json.loads(response.data) == {"sku": "12345", "message": "product 12345 created"}

def test_create_existing_product(client):
    
    data = {
        "name": "Product 2",
        "brand": "Brand 2",
        "weight": 20,
        "sku": "67890",
        "available": False
    }
    client.post('/products', json=data)

    data = {
        "name": "Product 3",
        "brand": "Brand 3",
        "weight": 30,
        "sku": "67890",
        "available": True
    }
    response = client.post('/products', json=data)
    assert response.status_code == 409
    assert json.loads(response.data) == {"sku": "67890", "message": "product 67890 already exists"}

def test_get_existing_product(client):
    data = {
        "name": "Product 4",
        "brand": "Brand 4",
        "weight": 40,
        "sku": "55555",
        "available": True
    }
    client.post('/products', json=data)

    response = client.get('/products/55555')
    assert response.status_code == 200
    assert json.loads(response.data) == {
        "name": "Product 4",
        "brand": "Brand 4",
        "weight": 40,
        "sku": "55555",
        "available": True
    }

def test_get_nonexistent_product(client):
    response = client.get('/products/99999')
    assert response.status_code == 404

def test_delete_existing_product(client):
    data = {
        "name": "Product 5",
        "brand": "Brand 5",
        "weight": 50,
        "sku": "77777",
        "available": True
    }
    client.post('/products', json=data)

    response = client.delete('/products/77777')
    assert response.status_code == 200

def test_delete_nonexistent_product(client):
    response = client.delete('/products/99999')
    assert response.status_code == 404

def test_update_existing_product(client):
    data = {
        "name": "Product 6",
        "brand": "Brand 6",
        "weight": 60,
        "sku": "88888",
        "available": True
    }
    client.post('/products', json=data)

    update_data = {
        "name": "Updated Product 6",
        "brand": "Updated Brand 6",
        "weight": 70,
        "sku": "88888",
        "available": False
    }
    response = client.patch('/products/88888', json=update_data)
    assert response.status_code == 200
    assert json.loads(response.data) == {"sku": "88888", "message": "product 88888 updated"}

def test_update_nonexistent_product(client):
    update_data = {
        "name": "Updated Product 7",
        "brand": "Updated Brand 7",
        "weight": 80,
        "sku": "99999",
        "available": True
    }
    response = client.patch('/products/99999', json=update_data)
    assert response.status_code == 404
