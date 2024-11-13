from typing import List
from decimal import Decimal
from pydantic import BaseModel
from typing import NamedTuple

from ....core.models._product import Product


class FilterProductsByStatusResponse(BaseModel):
    products: List[Product]