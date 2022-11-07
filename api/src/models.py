from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class Movimentacao(Base):
    __tablename__ = "movimentacao"
    estoque = relationship("Estoque", back_populates="movimentacao")

    movimentacao_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("estoque.id"))
    quantity = Column(Integer)


class Estoque(Base):
    __tablename__ = "estoque"
    movimentacao = relationship("Movimentacao", back_populates="estoque", cascade="all, delete")

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), index=True)
    description = Column(String(255), index=True)
    price = Column(Float, index=True, default=0)
    quantity = Column(Integer, primary_key = True, index=True, default=0)
    available = Column(Boolean, default=True)