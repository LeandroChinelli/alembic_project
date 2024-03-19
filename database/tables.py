from typing_extensions import Annotated
from typing import Optional
from sqlalchemy import ForeignKey, BIGINT, String, INTEGER
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import func
import datetime
from .connection import engine


# Creating a base class
class Base(DeclarativeBase):
    pass

# Users ForeignKey
user_fk = Annotated[
    int, mapped_column(BIGINT, ForeignKey("users.telegram_id", ondelete="CASCADE"))
]

# integer primary key
int_pk = Annotated[int, mapped_column(INTEGER, primary_key=True)]

# string column with length 255
str_255 = Annotated[str, mapped_column(String(255))]


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"
    

class User(Base, TimestampMixin, TableNameMixin):
    telegram_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    full_name: Mapped[str_255]
    username: Mapped[Optional[str_255]]
    language_code: Mapped[str_255]
    referrer_id: Mapped[Optional[user_fk]]
    

class Order(Base, TimestampMixin, TableNameMixin):
    order_id: Mapped[int_pk]
    user_id: Mapped[user_fk]


class Product(Base, TimestampMixin, TableNameMixin):
    product_id: Mapped[int_pk]
    title: Mapped[str_255]
    description: Mapped[str]


class OrderProduct(Base, TableNameMixin):

    order_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("orders.order_id", ondelete="CASCADE"), primary_key=True)
    product_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("products.product_id", ondelete="RESTRICT"), primary_key=True)
    quantity: Mapped[int]


# Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)