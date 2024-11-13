from .base import RepositoryConfig
from factories.repositories import sql_product_repository


class CatalogRepositoryConfig(RepositoryConfig):
    _AVAILABLE_REPOSITORIES: list[str] = ["SQL"]

    @classmethod
    def _get_repository_instances(cls) -> dict:
        return {"SQL": sql_product_repository()}
