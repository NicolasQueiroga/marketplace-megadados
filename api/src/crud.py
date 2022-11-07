from sqlalchemy.orm import Session

import api.src.models
import api.src.schemas


def get_product(db: Session, product_id: int):
    return db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == product_id).first()

def get_product_by_name(db: Session, name: str):
    return db.query(api.src.models.Estoque).filter(api.src.models.Estoque.name == name).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(api.src.models.Estoque).offset(skip).limit(limit).all() 

def create_product(db: Session, product: api.src.schemas.EstoqueCreate):
    db_product = api.src.models.Estoque(**product.dict())
    try:
        db.add(db_product)
        db.commit()
    except:
        db.rollback()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == product_id).first()

    try:
        db.delete(db_product)
        db.commit()
    except:
        db.rollback()

    return db_product

def update_product(db: Session, product: api.src.schemas.EstoqueUpdate, product_id: int):
    db_product = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == product_id).first()
    try:
        db_product.name = product.name
        db_product.description = product.description
        db_product.available = product.available
        db_product.price = product.price
        db.commit()
    except:
        db.rollback()
    db.refresh(db_product)
    return db_product

def update_product_by_movimentacao(db: Session, movimentacao: api.src.schemas.MovimentacaoCreate):
    db_product = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == movimentacao.product_id).first()
    try:
        db_product.quantity += movimentacao.quantity
        db.commit()
    except:
        db.rollback()
    db.refresh(db_product)
    return db_product

def create_movimentacao(db: Session, movimentacao: api.src.schemas.MovimentacaoCreate):
    db_movimentacao = api.src.models.Movimentacao(**movimentacao.dict())
    try:
        db.add(db_movimentacao)
        update_product_by_movimentacao(db, movimentacao)
        db.commit()
    except:
        db.rollback()
    db.refresh(db_movimentacao)
    return db_movimentacao


def get_movimentacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(api.src.models.Movimentacao).offset(skip).limit(limit).all()


def get_movimentacao(db: Session, movimentacao_id: int):
    return db.query(api.src.models.Movimentacao).filter(api.src.models.Movimentacao.movimentacao_id == movimentacao_id).first()


def update_movimentacao(db: Session, movimentacao_id: int,  movimentacao: api.src.schemas.MovimentacaoCreate):
    db_movimentacao_updated = api.src.models.Movimentacao(**movimentacao.dict())
    db_movimentacao = db.query(api.src.models.Movimentacao).filter(api.src.models.Movimentacao.movimentacao_id == movimentacao_id).first()
    
    db_product_updated = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == db_movimentacao_updated.product_id).first()
    db_product = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == db_movimentacao.product_id).first()
    
    try:
        db_product.quantity -= db_movimentacao.quantity
        
        if db_product.id != db_product_updated.id:
            db_product_updated.quantity += db_movimentacao_updated.quantity
        else:
            db_product.quantity += db_movimentacao_updated.quantity

        db_movimentacao.id = movimentacao_id
        db_movimentacao.product_id = db_movimentacao_updated.product_id
        db_movimentacao.quantity = db_movimentacao_updated.quantity
        
        db.commit()
    except:
        db.rollback()

    return db_movimentacao


def delete_movimentacao(db: Session, movimentacao_id: int):
    db_movimentacao = db.query(api.src.models.Movimentacao).filter(api.src.models.Movimentacao.movimentacao_id == movimentacao_id).first()
    db_product = db.query(api.src.models.Estoque).filter(api.src.models.Estoque.id == db_movimentacao.product_id).first()
    try:
        db_product.quantity -= db_movimentacao.quantity
        db.delete(db_movimentacao)
        db.commit()
    except:
        db.rollback()

    return db_movimentacao