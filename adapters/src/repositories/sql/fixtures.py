import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.src.repositories import SQLProductRepository
from adapters.src.repositories.sql.tables import Base

@pytest.fixture(scope="module")
def session():
    engine = create_engine("sqlite:///:memory:",
                           connect_args={'check_same_thread': False})
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()
    engine.dispose()


@pytest.fixture()
def product_repository(session):
    yield SQLProductRepository(session)