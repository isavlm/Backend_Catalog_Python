from typing import List
from pydantic import BaseModel

from ....core.models._product import Product


class ListProductResponse(BaseModel):
    products: List[Product]
