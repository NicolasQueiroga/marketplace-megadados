from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {
        "products": [
            {"product_id": 1,
            "product": {
                "name": "Shampoo",
                "description": "Cabelos cacheados",
                "price": 78.99,
                "quantity": 10,
            }
            },
            {"product_id": 2,
            "product": {
                "name": "Bolo de chocolate",
                "description": "Bolo de chocolate com cobertura de chocolate",
                "price": 18.90,
                "quantity": 8,
            }
            },
            {"product_id": 3,
            "product": {
                "name": "Iphone 13",
                "description": "Iphone 13 com 128GB de memória",
                "price": 9999.99,
                "quantity": 5,
            }
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


# def test_create_product():
#     response = client.post(
#         "/products",
#         json={
#             "name": "Arroz",
#             "description": "Arroz branco",
#             "price": 5.99,
#             "quantity": 23,
#         },
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Arroz",
#         "description": "Arroz branco",
#         "price": 5.99,
#         "quantity": 23,
#     }


# def test_update_product():
#     response = client.put(
#         "/products/1",
#         json={
#             "name": "Shampoo",
#             "description": "Cabelos loiros cacheados",
#             "price": 78.49,
#             "quantity": 9,
#         },
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "name": "Shampoo",
#         "description": "Cabelos loiros cacheados",
#         "price": 78.49,
#         "quantity": 9,
#     }

# def test_delete_product():
#     response = client.delete("/products/1")
#     assert response.status_code == 200
#     assert response.json() == {"task": "delete successful"}