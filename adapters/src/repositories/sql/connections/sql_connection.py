from adapters.src.repositories.config.sql import SQLConfig

from .connection import Connection


class SQLConnection(Connection):
    def get_connection_string(self) -> str:
        return f"{SQLConfig.DB_CONFIG}"
