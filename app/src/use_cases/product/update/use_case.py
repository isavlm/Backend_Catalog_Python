from .request import UpdateProductRequest
from .response import UpdateProductResponse
#from app.src.repositories import ProductRepository

from typing import Any, Optional

from app.src.exceptions import (
    ProductNotFoundException,
    ProductRepositoryException,
)

from app.src.core.models import Product
from app.src.repositories import ProductRepository


class UpdateProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __verify_product_exists(
        self, product: Optional[Product], request_entity_id: str
    ) -> None:
        if product is None:
            raise ProductNotFoundException(product_id=request_entity_id)

    def __call__(
        self, product_id: str, request: UpdateProductRequest
    ) -> UpdateProductResponse:
        print("Product Updated Successfully:")
        try:
            existing_product = self.product_repository.get_by_id(product_id)
            print(existing_product)
            self.__verify_product_exists(
                existing_product, request_entity_id=request.product_id
            )
            response = self.product_repository.Update(request)
            
            return response
        except ProductRepositoryException as e:
            raise e 
        