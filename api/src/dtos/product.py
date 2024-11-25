from typing import List
from decimal import Decimal
from pydantic import BaseModel  # Can't figure out why can't import this.


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


class DeleteProductResponse(BaseModel):
    ...


class UpdateProductResponseDto(ProductBase):
    ...

class UpdateProductRequestDto(ProductBase):
    ...

class FilterProductsByStatusRequestDto(BaseModel):
    status: str

class FilterProductByStatusResponseDto(BaseModel):
    products: List[ProductBase]