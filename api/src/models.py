from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(default = "Nome", title="Nome do produto", max_length=255, example="Shampoo")
    description: str = Field(default = "description", title="Descrição do produto", max_length=255, example="Descrição do produto")
    price: float = Field(default = 10.0,  title = "Preço do produto", description="Preço não pode ser negativo", ge=0, example=15.90)
    quantity: int = Field(default = 1,  title = "Quantidade do produto", description="Quantidade não pode ser negativa", ge=0, example=3)
