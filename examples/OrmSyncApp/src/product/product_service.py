from .product_model import Product
from .product_entity import Product as ProductEntity
from functools import lru_cache
from config import config
from nest.core.decorators import db_request_handler, Injectable


@lru_cache()
@Injectable
class ProductService:
    def __init__(self):
        self.config = config
        self.session = self.config.get_db()

    @db_request_handler
    def add_product(self, product: Product):
        new_product = ProductEntity(**product.dict())
        self.session.add(new_product)
        self.session.commit()
        return new_product.id

    @db_request_handler
    def get_products(self):
        return self.session.query(ProductEntity).all()
