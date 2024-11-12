import pytest
from adapters.src.repositories.sql.tables.product import ProductSchema
from faker import Faker
from decimal import Decimal
from app.src.core.models._product import Product, ProductStatuses

from app.tests.fixtures.product_repository import mock_product_repository
from adapters.src.repositories.sql.test.fixtures import session, product_repository
from api.tests.fixtures import mock_session_manager, client, app

fake = Faker()


@pytest.fixture
def fake_product_list():
    return [Product(
        product_id=fake.uuid4(),
        user_id=fake.uuid4(),
        name=fake.word(),
        description=fake.sentence(),
        price=Decimal(fake.pyint(min_value=0, max_value=9999, step=1)),
        location=fake.address(),
        status=fake.random_element(elements=(
            ProductStatuses.NEW, ProductStatuses.USED, ProductStatuses.FOR_PARTS)),
        is_available=fake.boolean()
    ) for _ in range(2)]


@pytest.fixture
def fake_database_product_list():
    return [ProductSchema(
        product_id=fake.uuid4(),
        user_id=fake.uuid4(),
        name=fake.word(),
        description=fake.sentence(),
        price=Decimal(fake.pyint(min_value=0, max_value=9999, step=1)),
        location=fake.address(),
        status=fake.random_element(elements=("New", "Used", "For parts")),
        is_available=fake.boolean()
    ) for _ in range(2)]


@pytest.fixture
def fake_product():
    return Product(
        product_id=fake.uuid4(),
        user_id=fake.uuid4(),
        name=fake.word(),
        description=fake.sentence(),
        price=Decimal(fake.pyint(min_value=0, max_value=9999, step=1)),
        location=fake.address(),
        status=fake.random_element(elements=(
            ProductStatuses.NEW, ProductStatuses.USED, ProductStatuses.FOR_PARTS)),
        is_available=fake.boolean()
    )
