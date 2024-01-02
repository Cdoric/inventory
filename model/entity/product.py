from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from model.entity import *


class Product(Base):
    __tablename__ = "product_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    brand = Column(String(30))
    price = Column(Integer)

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
#product ==> store-product