from .example_model import Example
from .example_entity import Example as ExampleEntity
from config import config
from nest.core.decorators import db_request_handler
from functools import lru_cache
from nest.core.decorators import Injectable


@lru_cache()
@Injectable
class ExampleService:
    def __init__(self):
        self.config = config
        self.session = self.config.get_db()

    @db_request_handler
    def add_example(self, example: Example):
        new_example = ExampleEntity(**example.dict())
        self.session.add(new_example)
        self.session.commit()
        return new_example.id

    @db_request_handler
    def get_example(self):
        return self.session.query(ExampleEntity).all()
