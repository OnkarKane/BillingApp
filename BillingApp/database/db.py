
import mysql.connector

class DBHelper:
    def __init__(self, host="localhost", user="root", password="", database="BillingDB"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,  
            database=database
        )
        self.cursor = self.conn.cursor()

    def insert_customer(self, name, phone):
        query = "INSERT INTO customers (name, phone) VALUES (%s, %s)"
        values = (name, phone)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_bill(self, customer_id, product_name, quantity, price, total):
        query = """
        INSERT INTO bills (customer_id, product_name, quantity, price, total)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (customer_id, product_name, quantity, price, total)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_all_bills(self):
        query = """
        SELECT b.id, c.name, c.phone, b.product_name, b.quantity, b.price, b.total
        FROM bills b
        JOIN customers c ON b.customer_id = c.id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
