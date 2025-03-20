
from PySide6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox)
from models.billing_model import BillingModel

class BillingForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billing System")
        self.setGeometry(100, 100, 600, 400)
        
        self.model = BillingModel()

        # Widgets
        self.name_label = QLabel("Customer Name:")
        self.name_input = QLineEdit()

        self.phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()

        self.product_label = QLabel("Product Name:")
        self.product_input = QLineEdit()

        self.quantity_label = QLabel("Quantity:")
        self.quantity_input = QLineEdit()

        self.price_label = QLabel("Price per Unit:")
        self.price_input = QLineEdit()

        self.submit_btn = QPushButton("Submit Bill")
        self.submit_btn.clicked.connect(self.submit_bill)

        self.show_btn = QPushButton("Show All Bills")
        self.show_btn.clicked.connect(self.show_bills)

        # Table to display bills
        self.bill_table = QTableWidget()
        self.bill_table.setColumnCount(7)
        self.bill_table.setHorizontalHeaderLabels(["ID", "Customer Name", "Phone", "Product", "Quantity","Price per Unit", "Total"])

        # Layout
        form_layout = QVBoxLayout()
        form_layout.addWidget(self.name_label)
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.phone_label)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(self.product_label)
        form_layout.addWidget(self.product_input)
        form_layout.addWidget(self.quantity_label)
        form_layout.addWidget(self.quantity_input)
        form_layout.addWidget(self.price_label)
        form_layout.addWidget(self.price_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_btn)
        button_layout.addWidget(self.show_btn)

        form_layout.addLayout(button_layout)
        form_layout.addWidget(self.bill_table)

        self.setLayout(form_layout)

    def submit_bill(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        product_name = self.product_input.text()
        quantity = int(self.quantity_input.text())
        price = float(self.price_input.text())
        total = quantity * price

        if not name or not phone or not product_name:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        try:
            customer_id = self.model.add_customer(name, phone)
            self.model.add_bill(customer_id, product_name, quantity, price, total)
            QMessageBox.information(self, "Success", "Bill added successfully!")
            self.clear_form()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add bill. Error: {str(e)}")

    def show_bills(self):
        bills = self.model.get_all_bills()
        self.bill_table.setRowCount(len(bills))
        for row_num, row_data in enumerate(bills):
            for col_num, data in enumerate(row_data):
                self.bill_table.setItem(row_num, col_num, QTableWidgetItem(str(data)))

    def clear_form(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.product_input.clear()
        self.quantity_input.clear()
        self.price_input.clear()
