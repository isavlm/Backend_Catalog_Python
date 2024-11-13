from abc import ABC, abstractmethod
from typing import List, Optional

from ..core.models import Product


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[Product]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def edit(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: str) -> Product:
        raise NotImplementedError
