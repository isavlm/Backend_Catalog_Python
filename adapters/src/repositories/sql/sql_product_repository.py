from typing import List, Optional
from decimal import Decimal
from sqlalchemy.orm import Session
from app.src import Product, ProductRepository, ProductRepositoryException
from .tables import ProductSchema
from sqlalchemy.inspection import inspect



class SQLProductRepository(ProductRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_all(self) -> List[Product]:
        try:
            with self.session as session:
                products = session.query(ProductSchema).all()
                if products is None:
                    return []
                product_list = [
                    Product(
                        product_id=str(product.product_id),
                        user_id=str(product.user_id),
                        name=str(product.name),
                        description=str(product.description),
                        price=Decimal(product.price),
                        location=str(product.location),
                        status=str(product.status),
                        is_available=bool(product.is_available),
                    )
                    for product in products
                ]
                return product_list
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="list")

    def create(self, product: Product) -> Product:
        try:
            product_to_create = ProductSchema(
                product_id=product.product_id,
                user_id=product.user_id,
                name=product.name,
                description=product.description,
                price=product.price,
                location=product.location,
                status=product.status,
                is_available=product.is_available,
            )
            with self.session as session:
                session.add(product_to_create)
                session.commit()
            return product
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="create")

    def get_by_id(self, product_id: str) -> Optional[Product]:
        try:
            with self.session as session:
                product = (
                    session.query(ProductSchema)
                    .filter(ProductSchema.product_id == product_id)
                    .first()
                )
                if product is None:
                    return None
                return Product(
                    product_id=str(product.product_id),
                    user_id=str(product.user_id),
                    name=str(product.name),
                    description=str(product.description),
                    price=Decimal(product.price),
                    location=str(product.location),
                    status=str(product.status),
                    is_available=bool(product.is_available),
                )
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="find")

#Isadora's Code starts here


    def update(self, product: Product) -> Product:
        try:
            with self.session as session:
                existing_product = (session.query(ProductSchema).filter(
                    ProductSchema.product_id == product.product_id).first())
                
                if existing_product is None:
                    raise ProductRepositoryException(
                        method="update", message="Product not found")
                
                session.query(ProductSchema).filter(
                    ProductSchema.product_id == product.product_id).update({
                        "user_id": product.user_id,
                        "name": product.name,
                        "description": product.description,
                        "price": product.price,
                        "location": product.location,
                        "status": product.status,
                        "is_available": product.is_available
                    }) 
                
                session.commit()

            #Printing a success message before returning the product
            print(f"Product updated successfully: {product}")   
            return product
        except Exception as e:
            self.session.rollback()
            # print the original exception message
            print(f"Error occurred: {str(e)}")
            raise ProductRepositoryException(method="update", message=str(e))



    def delete(self, product_id: str) -> Product:
        try:
            with self.session as session:
                session.query(ProductSchema).filter(
                    ProductSchema.product_id == product_id).delete()
                session.commit()
            return product_id
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="delete")
        

    def filter(self, status: str) -> List[Product]:
        try:
            with self.session as session:
                # Query to filter products by status and return a list of results
                products = session.query(ProductSchema).filter(ProductSchema.status == status).all()

                if not products:
                    print(f"No products found with status: {status}")
                    return []

                # Return the list of products converted to Product model
                return [
                    Product(
                        product_id=str(product.product_id),
                        user_id=str(product.user_id),
                        name=str(product.name),
                        description=str(product.description),
                        price=Decimal(product.price),
                        location=str(product.location),
                        status=str(product.status),
                        is_available=bool(product.is_available),
                    )
                    for product in products
                ]
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="get_by_status")