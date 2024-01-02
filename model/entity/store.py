from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.entity import *


class Store(Base):
    __tablename__ = "store_tbl"

    # id, product, quantity
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    quantity = Column(Integer)

    product = relationship("Product")

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
