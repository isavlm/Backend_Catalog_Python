from typing import List
from decimal import Decimal
from pydantic import BaseModel


class ProductBase(BaseModel):
    product_id: str
    user_id: str
    name: str
    description: str | None
    price: Decimal
    location: str
    status: str
    is_available: bool


class ListProductResponseDto(BaseModel):
    products: List[ProductBase]


class FindProductByIdResponseDto(ProductBase):
    ...


class CreateProductRequestDto(ProductBase):
    ...


class CreateProductResponseDto(ProductBase):
    ...
