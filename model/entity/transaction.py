from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.entity import *


class Transaction(Base):
    __tablename__ = "transaction_tbl"

    # id,customer,product,date_time
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customer_tbl.id"))
    product_id = Column(Integer, ForeignKey("product_tbl.id"))
    date_time = Column(DateTime)
    quantity = Column(Integer)
    customer = relationship("Customer")
    product = relationship("Product")

    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.date_time = datetime.now()
        self.quantity = quantity
