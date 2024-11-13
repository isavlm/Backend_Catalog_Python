from adapters.src.repositories import SQLProductRepository, SessionManager
from app.src.repositories import ProductRepository


def sql_product_repository() -> ProductRepository:
    return SQLProductRepository(SessionManager.get_session())
