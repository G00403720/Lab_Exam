from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False)
    customer_since = mapped_column(Integer, nullable=False)

class Order(Base):
    __tablename__ = "orders"
    id = mapped_column(Integer, primary_key=True)
    order_number = mapped_column(Integer, nullable=False)
    total_cents = mapped_column(Integer, nullable=False)
    customer_id = relationship(cascade="delete on customer removal")
  