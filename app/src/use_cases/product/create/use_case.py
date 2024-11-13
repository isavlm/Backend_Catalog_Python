from typing import Optional

from app.src.core import Product
from app.src.repositories import ProductRepository
from app.src.exceptions import (
    ProductAlreadyExistsException,
    ProductNoneException,
    ProductRepositoryException,
    ProductBusinessException,
)

from .response import CreateProductResponse
from .request import CreateProductRequest


class CreateProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(
        self, request: CreateProductRequest
    ) -> Optional[CreateProductResponse]:
        product = Product(**request._asdict())
        try:
            product_existing = self.product_repository.get_by_id(request.product_id)
            if product_existing:
                raise ProductAlreadyExistsException(product_id=request.product_id)
            response: Optional[Product] = self.product_repository.create(product)
            if not response:
                raise ProductNoneException()

            return CreateProductResponse(**response._asdict())
        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))
