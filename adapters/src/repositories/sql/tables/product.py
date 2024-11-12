from sqlalchemy import Column, String, Boolean, Numeric

from .base import Base


class ProductSchema(Base):
    __tablename__ = "products"
    product_id = Column(String, primary_key=True)
    user_id = Column(String)
    name = Column(String)
    description = Column(String)
    price = Column(Numeric)
    location = Column(String)
    status = Column(String)
    is_available = Column(Boolean)
