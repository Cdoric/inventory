
from model.da import *


class CustomerController:
    @classmethod
    def save(cls, name, family, username, password):
        try:
            da = CustomerDa()
            customer = Customer(name, family, username, password)
            return True, da.save(customer)
        except Exception as e:
            return False, str(e)


    @classmethod
    def edit(cls,id, name, family, username, password):
        try:
            da = CustomerDa()
            customer = Customer(name, family, username, password)
            customer.id = id
            return True, da.edit(customer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = CustomerDa()
            return True, da.remove(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CustomerDa()
            return True, da.find_all(Customer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = CustomerDa()
            return True, da.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = CustomerDa()
            return True, da.find_by_username(name)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_family(cls, family):
        try:
            da = CustomerDa()
            return True, da.find_by_family(family)
        except Exception as e:
            return False, str(e)
