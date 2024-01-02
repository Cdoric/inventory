from model.da.database import *
from model.entity import *


class StoreDa(DataBaseManager):
    def find_by_product(self,product):
        self.make_engine()
        result = self.session.query(Store).filter(Store.product == product)
        self.session.close()
        return result

    def remove(self, id):
        return self.remove_by_id(Store, id)
