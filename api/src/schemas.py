from pydantic import BaseModel, Field

class EstoqueBase(BaseModel):
    name: str = Field(default = "ProductName", title="Nome do produto", max_length=255, example="Shampoo")
    description: str = Field(default = "ProductDescription", title="Descrição do produto", max_length=255, example="Shampoo para cabelos secos")
    price: float = Field(default = 0.0, title="Preço do produto", example=10.0)


class EstoqueCreate(EstoqueBase):
    pass


class EstoqueUpdate(EstoqueBase):
    available: bool = Field(default = True, title="Disponibilidade do produto",description="Disponibilidade do produto", example=True)


class Estoque(EstoqueBase):
    id: int = Field(default = 0, title="ID do produto", description="ID do produto", example=1)
    quantity: int = Field(default = 0, title="Quantidade do produto",description="Quantidade do produto", example=10)
    available: bool = Field(default = True, title="Disponibilidade do produto",description="Disponibilidade do produto", example=True)

    class Config:
        orm_mode = True


class MovimentacaoBase(BaseModel):
    product_id: int = Field(default = None, title="ID do produto",description="ID do produto", example=1)
    quantity: int = Field(default = 1, title="Quantidade do produto",description="Quantidade do produto", example=1)

class MovimentacaoCreate(MovimentacaoBase):
    pass


class Movimentacao(MovimentacaoBase):
    movimentacao_id: int = Field(default = None, title="ID da movimentação",description="ID da movimentação", example=1)
    class Config:
        orm_mode = True