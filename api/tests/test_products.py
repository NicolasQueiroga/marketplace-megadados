from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()['status'] == "healthy"


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {
        "products": [
            {
                "name": "Shampoo",
                "description": "Cabelos cacheados",
                "price": 78.99,
                "quantity": 10,
            },
            {
                "name": "Bolo de chocolate",
                "description": "Bolo de chocolate com cobertura de chocolate",
                "price": 18.9,
                "quantity": 8,
            },
            {
                "name": "Iphone 13",
                "description": "Iphone 13 com 128GB de memória",
                "price": 9999.99,
                "quantity": 5,
            },
        ]
    }


def test_get_product():
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Shampoo",
        "description": "Cabelos cacheados",
        "price": 78.99,
        "quantity": 10,
    }