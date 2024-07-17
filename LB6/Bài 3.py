import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QLineEdit, QComboBox, QSpinBox, QCheckBox, 
                             QPushButton, QGroupBox, QFormLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class DataEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Data Entry Form')
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: #f0f0f0;")

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        title_label = QLabel("Data Entry Form")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # User Information
        user_group = QGroupBox("User Information")
        user_layout = QFormLayout()

        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.title = QComboBox()
        self.title.addItems(["Mr.", "Mrs.", "Ms.", "Dr.", "Prof."])
        self.age = QSpinBox()
        self.age.setRange(1, 120)
        self.age.setValue(18)
        self.nationality = QLineEdit()

        user_layout.addRow("First Name:", self.first_name)
        user_layout.addRow("Last Name:", self.last_name)
        user_layout.addRow("Title:", self.title)
        user_layout.addRow("Age:", self.age)
        user_layout.addRow("Nationality:", self.nationality)

        user_group.setLayout(user_layout)
        main_layout.addWidget(user_group)

        # Registration Status
        reg_group = QGroupBox("Registration Status")
        reg_layout = QVBoxLayout()

        self.currently_registered = QCheckBox("Currently Registered")
        reg_layout.addWidget(self.currently_registered)
        
        courses_layout = QHBoxLayout()
        courses_layout.addWidget(QLabel("# Completed Courses"))
        self.completed_courses = QSpinBox()
        courses_layout.addWidget(self.completed_courses)
        reg_layout.addLayout(courses_layout)

        semesters_layout = QHBoxLayout()
        semesters_layout.addWidget(QLabel("# Semesters"))
        self.semesters = QSpinBox()
        semesters_layout.addWidget(self.semesters)
        reg_layout.addLayout(semesters_layout)

        reg_group.setLayout(reg_layout)
        main_layout.addWidget(reg_group)

        # Terms & Conditions
        terms_group = QGroupBox("Terms & Conditions")
        terms_layout = QVBoxLayout()
        self.accept_terms = QCheckBox("I accept the terms and conditions.")
        terms_layout.addWidget(self.accept_terms)
        terms_group.setLayout(terms_layout)
        main_layout.addWidget(terms_group)

        # Submit Button
        self.submit_button = QPushButton("Enter data")
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 5px 15px;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.submit_button.clicked.connect(self.submit_data)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

    def submit_data(self):
        if not self.accept_terms.isChecked():
            print("Please accept the terms and conditions.")
            return
        
        print("Data submitted:")
        print(f"Name: {self.first_name.text()} {self.last_name.text()}")
        print(f"Title: {self.title.currentText()}")
        print(f"Age: {self.age.value()}")
        print(f"Nationality: {self.nationality.text()}")
        print(f"Currently Registered: {'Yes' if self.currently_registered.isChecked() else 'No'}")
        print(f"Completed Courses: {self.completed_courses.value()}")
        print(f"Semesters: {self.semesters.value()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DataEntryForm()
    ex.show()
    sys.exit(app.exec_())