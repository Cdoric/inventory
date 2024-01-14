from model.entity import *
from model.da import *


class TransactionController:
    @classmethod
    def save(cls, customer, product, quantity):
        try:
            da = TransactionDa()
            transaction = Transaction(customer, product, quantity)
            da.save(transaction)
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, customer, product, quantity):
        try:
            da = ProductDa()
            transaction = Transaction(customer, product, quantity)
            transaction.id = id
            da.edit(transaction)
            return True, transaction
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = TransactionDa()
            transaction = da.find_by_ID(Transaction, id)
            if transaction:
                da.remove(transaction)
                return True
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = TransactionDa()
            return True, da.find_all(Transaction)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = TransactionDa()
            return True, da.find_by_ID(id)
        except Exception as e:
            return False, str(e)

    def find_by_customer(self, customer):
        try:
            da = TransactionDa()
            return True, da.find_by_customer(customer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_product(cls, product):
        try:
            da = TransactionDa()
            return True, da.find_by_product(product)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_time(cls, datetime1, datetime2):
        try:
            da = TransactionDa()
            transacaion_list = da.find_by_time(datetime1, datetime2)
            return transacaion_list
        except Exception as e:
            return False, str(e)
