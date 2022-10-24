from fastapi import FastAPI
from .models import Product
from .database import products_db
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler



app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Marketplace - MEGADADOS",
        version="1.0.0",
        description="Custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = custom_openapi


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)


@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the Marketplace - MEGADADOS API",
        "status": "healthy"
    }

@app.get("/products", status_code=201, response_model = Product, tags=["Get All Products"])
async def get_products():
    return {"products": products_db}


@app.get("/products/{product_id}", status_code=200, response_model = Product, tags=["Get Product From ID"])
async def get_product(product_id: int):
    return products_db[product_id - 1]
