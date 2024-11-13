from app.src.exceptions.repository.product import ProductRepositoryException
from app.src.repositories import ProductRepository
from .response import ListProductResponse


class ListProducts:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self) -> ListProductResponse:
        try:
            products = self.product_repository.list_all()
            return ListProductResponse(products=products)
        except ProductRepositoryException as error:
            raise ProductRepositoryException(str(error))
