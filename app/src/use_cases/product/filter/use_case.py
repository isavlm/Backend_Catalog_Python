from app.src.exceptions import (
    ProductRepositoryException,
    ProductNotFoundException,
)
from app.src.core.models import Product
from app.src.repositories import ProductRepository
from .request import FilterProductsByStatusRequest
from .response import FilterProductsByStatusResponse


class FilterProductByStatus:

    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __call__(
        self, request: FilterProductsByStatusRequest
    ) -> FilterProductsByStatusResponse:
        try:
            existing_products = self.product_repository.filter(
                request.status
            )
            
            response = FilterProductsByStatusResponse(
                products=existing_products
            )
            return response
        except ProductRepositoryException as e:
            raise e
        