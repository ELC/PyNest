from .user_model import User
from .user_entity import User as UserEntity
from config import config
from nest.core.decorators import db_request_handler, Injectable
from functools import lru_cache


@lru_cache()
@Injectable
class UserService:
    def __init__(self):
        self.config = config
        self.session = self.config.get_db()

    @db_request_handler
    def add_user(self, user: User):
        new_user = UserEntity(**user.dict())
        self.session.add(new_user)
        self.session.commit()
        return new_user.id

    @db_request_handler
    def get_users(self):
        return self.session.query(UserEntity).all()
