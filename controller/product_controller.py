from model.da import *


class ProductController:
    @classmethod
    def save(cls, name, brand, price):
        try:
            da = ProductDa()
            product = Product(name, brand, price)
            da.save(product)
            return True, product
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, brand, price):
        try:
            da = ProductDa()
            product = Product(name, brand, price)
            product.id = id
            da.edit(product)
            return True, product
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProductDa()
            da.remove_by_ID(id)
            # product = da.find_by_ID(Product, id)
            # print("Product : ",product)
            # if product:
            #     da.remove(product)
            return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProductDa()
            product_list = da.find_by_ID(id)
            return True, product_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_name(cls, name):
        try:
            da = ProductDa()
            product_list = da.find_by_name(name)
            return True, product_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_brand(cls, brand):
        try:
            da = ProductDa()
            product_list = da.find_by_brand(brand)
            return True, product_list
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProductDa()
            return True, da.find_all(Product)
        except Exception as e:
            return False, str(e)
