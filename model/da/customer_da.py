from model.da.database import *
from model.entity import *


class CustomerDa(DataBaseManager):
    def find_by_id(self, id):
        return self.find_by_ID(Customer, id)

    def remove(self, id):
        return self.remove_by_id(Customer, id)

    def find_by_name(self):
        self.make_engine()
        result = self.session.query(customer).filter(Customer.name == name)
        self.session.close()
        return result
