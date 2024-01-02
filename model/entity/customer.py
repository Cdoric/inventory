from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"

    # id,name,family,username,password
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    family = Column(String(20))
    username = Column(String(20))  # todo validator username
    password = Column(String(20))  # todo validator password
    # role = Column(String(10))

    def __init__(self, name, family, username, password):
        self.name = name
        self.family = family
        self.username = username
        self.password = password
