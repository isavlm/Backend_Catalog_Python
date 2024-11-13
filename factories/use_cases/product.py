from app.src.repositories import ProductRepository
from factories.repositories import sql_product_repository
from app.src.use_cases import ListProducts, FindProductById, CreateProduct


def get_product_repository() -> ProductRepository:
    return sql_product_repository()


def list_product_use_case() -> ListProducts:
    return ListProducts(get_product_repository())


def find_product_by_id_use_case() -> FindProductById:
    return FindProductById(get_product_repository())


def create_product_use_case() -> CreateProduct:
    return CreateProduct(get_product_repository())
