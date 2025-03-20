# main.py
import sys
from PySide6.QtWidgets import QApplication
from forms.billing_form import BillingForm

def main():
    app = QApplication(sys.argv)
    window = BillingForm()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
