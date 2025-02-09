from config import config
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Product(config.Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True)
