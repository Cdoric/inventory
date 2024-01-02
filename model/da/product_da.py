from model.da.database import *
from model.entity import Product


class ProductDa(DataBaseManager):
    def find_by_ID(self, id):
        self.make_engine()
        result = self.session.query(Product).filter(Product.id == id).all()
        self.session.close()
        return result

    # todo filter
    def find_by_name(self, name):
        self.make_engine()
        result = self.session.query(Product).filter(Product.name == name)
        self.session.close()
        return result

    def remove(self, id):
        return self.remove_by_id(Product, id)

