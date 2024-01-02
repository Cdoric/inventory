from model.da import StoreDa
from model.entity import *


class StoreController:
    # todo
    @classmethod
    def save(cls, product, quantity):
        try:
            da = StoreDa()
            store = Store(product, quantity)
            da.save(product)
            return True, product
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, product, quantity):
        try:
            da = StoreDa()
            store = Store(id, product, quantity)
            da.edit(store)
            return True, store
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, product):
        try:
            da = StoreDa()
            store = da.find_by_ID(Store, id)
            if product:
                da.remove(store)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = StoreDa()
            product_list = da.find_by_ID(id)
            return True, product_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = StoreDa()
            product_list = da.find_by_name(name)
            return True, product_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = StoreDa()
            product_list = da.find_by_brand(brand)
            return True, product_list
        except Exception as e:
            return False, str(e)
