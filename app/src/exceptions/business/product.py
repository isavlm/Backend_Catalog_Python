from .base import (
    AlreadyExistsException,
    BusinessException,
    NoneException,
    NotFoundException,
)


class ProductBusinessException(BusinessException):
    """product Business exception"""


class ProductNotFoundException(NotFoundException):
    def __init__(self, product_id: str):
        super().__init__(entity_type="Product", entity_id=product_id)


class ProductAlreadyExistsException(AlreadyExistsException):
    def __init__(self, product_id: str) -> None:
        super().__init__(entity_type="Product", entity_id=product_id)


class ProductNoneException(NoneException):
    def __init__(self) -> None:
        super().__init__(entity_type="Product")
