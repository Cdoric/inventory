from model.da.database import *
from model.entity import *


class TransactionDa(DataBaseManager):
    def save(self, entity):
        self.make_engine()


        self.session =  self.session.object_session(entity)
        self.session.add(entity)
        self.session.commit()
