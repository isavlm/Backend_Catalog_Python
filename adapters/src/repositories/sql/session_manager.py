from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .connections import Connection
from .tables import Base


class SessionManager:
    _session = None
    _instance = None

    def __new__(cls) -> "SessionManager":
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize_session(cls, connection: Connection):
        engine = create_engine(connection.get_connection_string())
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine)
        cls._session = session_factory()

    @classmethod
    def get_session(cls) -> Session:
        if not cls._session:
            raise Exception("Database session has not been initialized.")
        return cls._session

    @classmethod
    def close_session(cls) -> None:
        if not cls._session:
            raise Exception("Database session has not been initialized to be closed.")
        cls._session.close()
        cls._session = None
