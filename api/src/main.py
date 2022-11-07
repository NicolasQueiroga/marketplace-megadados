from typing import List
from dotenv import load_dotenv
load_dotenv()

import api.src.crud
from api.src.models import Base 
import api.src.schemas
from api.src.database import SessionLocal, engine
from starlette.exceptions import HTTPException as StarletteHTTPException

from sqlalchemy.orm import Session

from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI, Request, Response, HTTPException, Depends
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Marketplace - MEGADADOS",
        version="2.0.0",
        description="API para o Marketplace da matéria de MEGADADOS",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await request_validation_exception_handler(request, exc)


def product_not_in_db(db : Session, product_id: int):
    if api.src.crud.get_product(db, product_id) is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

def movimentacao_not_in_db(db : Session, movimentacao_id: int):
    if api.src.crud.get_movimentacao(db, movimentacao_id) is None:
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")


@app.get("/",tags=["Main"])
async def read_root():
    return {
        "message": "Welcome to the Marketplace V2 - MEGADADOS API",
        "status": "healthy",
    }

# CRUD DE PRODUTOS
@app.get("/produtos", status_code=200, response_model=List[api.src.schemas.Estoque], tags=["Produtos"])
async def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna todos os produtos cadastrados no banco de dados
    skip: int = 0
    limit: int = 100
    """
    produtos = api.src.crud.get_products(db, skip=skip, limit=limit)
    return produtos

@app.get("/produtos/{product_id}", status_code=200, response_model=api.src.schemas.Estoque, tags=["Produtos"])
async def read_produto(product_id: int, db: Session = Depends(get_db)):
    """
    Retorna um produto específico
    product_id: int
    """
    product_not_in_db(db, product_id)
    produto = api.src.crud.get_product(db, product_id)
    return produto

@app.post("/produtos", status_code=201, response_model=api.src.schemas.Estoque, tags=["Produtos"])
async def create_produto(produto: api.src.schemas.EstoqueCreate, db: Session = Depends(get_db)):
    """
    Cria um produto
    produto: ProdutoCreate
    """
    db_produto = api.src.crud.get_product_by_name(db, name=produto.name)
    if db_produto:
        raise HTTPException(status_code=400, detail="Produto já cadastrado")
    return api.src.crud.create_product(db=db, product=produto)

@app.put("/produtos/{product_id}", status_code=200, response_model=api.src.schemas.Estoque, tags=["Produtos"])
async def update_produto(product_id: int, produto: api.src.schemas.EstoqueUpdate, db: Session = Depends(get_db)):
    """
    Atualiza um produto
    product_id: int
    produto: ProdutoCreate
    """
    product_not_in_db(db, product_id)
    db_produto = api.src.crud.get_product_by_name(db, name=produto.name)
    if db_produto and db_produto.id != product_id:
        raise HTTPException(status_code=400, detail="Produto já cadastrado")
    return api.src.crud.update_product(db=db, product_id=product_id, product=produto)

@app.delete("/produtos/{product_id}", status_code=200, response_model=api.src.schemas.Estoque, tags=["Produtos"])
async def delete_produto(product_id: int, db: Session = Depends(get_db)):
    """
    Deleta um produto
    product_id: int
    """
    product_not_in_db(db, product_id)
    return api.src.crud.delete_product(db=db, product_id=product_id)

# CRUD DE MOVIMENTAÇÕES
@app.get("/movimentacoes", status_code=200, response_model=List[api.src.schemas.Movimentacao], tags=["Movimentacoes"])
async def read_movimentacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna todas as movimentações cadastradas no banco de dados
    skip: int = 0
    limit: int = 100
    """
    movimentacoes = api.src.crud.get_movimentacoes(db, skip=skip, limit=limit)
    return movimentacoes

@app.get("/movimentacoes/{movimentacao_id}", status_code=200, response_model=api.src.schemas.Movimentacao, tags=["Movimentacoes"])
async def read_movimentacao(movimentacao_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma movimentação específica
    movimentacao_id: int
    """
    movimentacao_not_in_db(db, movimentacao_id)
    movimentacao = api.src.crud.get_movimentacao(db, movimentacao_id)
    return movimentacao


@app.post("/movimentacoes", status_code=201, response_model=api.src.schemas.Movimentacao, tags=["Movimentacoes"])
async def create_movimentacao(movimentacao: api.src.schemas.MovimentacaoCreate, db: Session = Depends(get_db)):
    """
    Cria uma movimentação
    movimentacao: MovimentacaoCreate
    """
    return api.src.crud.create_movimentacao(db=db, movimentacao=movimentacao)

@app.put("/movimentacoes/{movimentacao_id}", status_code=200, response_model=api.src.schemas.Movimentacao, tags=["Movimentacoes"])
async def update_movimentacao(movimentacao_id: int, movimentacao: api.src.schemas.MovimentacaoCreate, db: Session = Depends(get_db)):
    """
    Atualiza uma movimentação
    movimentacao_id: int
    movimentacao: MovimentacaoCreate
    """
    movimentacao_not_in_db(db, movimentacao_id)
    return api.src.crud.update_movimentacao(db=db, movimentacao_id=movimentacao_id, movimentacao=movimentacao)

@app.delete("/movimentacoes/{movimentacao_id}", status_code=200, response_model=api.src.schemas.Movimentacao, tags=["Movimentacoes"])
async def delete_movimentacao(movimentacao_id: int, db: Session = Depends(get_db)):
    """
    Deleta uma movimentação
    movimentacao_id: int
    """
    movimentacao_not_in_db(db, movimentacao_id)
    return api.src.crud.delete_movimentacao(db=db, movimentacao_id=movimentacao_id)