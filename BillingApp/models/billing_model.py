
from database.db import DBHelper

class BillingModel:
    def __init__(self):
        self.db = DBHelper()

    def add_customer(self, name, phone):
        return self.db.insert_customer(name, phone)

    def add_bill(self, customer_id, product_name, quantity, price, total):
        self.db.insert_bill(customer_id, product_name, quantity, price, total)

    def get_all_bills(self):
        return self.db.get_all_bills()
