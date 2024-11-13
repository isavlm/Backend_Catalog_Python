from .base import RepositoryException


class ProductRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Product", method=method)
