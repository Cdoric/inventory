from model.da.database import DataBaseManager
from model.entity import Customer

da=DataBaseManager()

customer = Customer("dorsa", "dorsa","user","password")
da.save(customer)
print(customer)

customer=Customer