from typing import Optional

from app.src.exceptions import ProductNotFoundException, ProductRepositoryException

from app.src.core.models import Product
from app.src.repositories import ProductRepository

from .request import FindProductByIdRequest
from .response import FindProductByIdResponse


class FindProductById:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __verify_product_exists(
        self, product: Optional[Product], request_entity_id: str
    ) -> None:
        if product is None:
            raise ProductNotFoundException(product_id=request_entity_id)

    def __call__(self, request: FindProductByIdRequest) -> FindProductByIdResponse:
        try:
            existing_product = self.product_repository.get_by_id(request.product_id)
            self.__verify_product_exists(
                existing_product, request_entity_id=request.product_id
            )
            response = FindProductByIdResponse(**existing_product._asdict())
            return response
        except ProductRepositoryException as e:
            raise e
