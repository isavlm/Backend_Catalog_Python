from copy import deepcopy

from adapters.src.repositories.sql.tables.product import ProductSchema


def test_list_all(product_repository, session, fake_database_product_list):

    [productA, productB] = fake_database_product_list
    session.add(productA)
    session.add(productB)
    session.commit()

    products = product_repository.list_all()
    assert len(products) == 2
    assert productA.name == products[0].name
    assert productB.name == products[1].name


def test_filter(product_repository, session, fake_database_product_list):
    [productA, productB] = fake_database_product_list
    session.add(productA)
    session.add(productB)
    session.commit()

    products = product_repository.filter("New")
    if len(products) > 0:
        for product in products:
            assert product.status == "New"
    else:
        assert products == []


def test_update(product_repository, session, fake_database_product_list):
    [productA, productB] = fake_database_product_list
    updated_product = deepcopy(productA)
    session.add(productA)
    session.add(productB)
    session.commit()

    updated_product.description = "Updated Description"
    product = product_repository.update(
        updated_product.product_id, updated_product)

    assert product.description == "Updated Description"


def test_delete(product_repository, session, fake_database_product_list):
    session.query(ProductSchema).delete()
    session.commit()
    [productA, productB] = fake_database_product_list
    product_deleted_id = productA.product_id
    session.add(productA)
    session.add(productB)
    session.commit()

    result = product_repository.delete(productA.product_id)
    list_of_products = product_repository.list_all()

    assert result == product_deleted_id
    assert len(list_of_products) == 1
