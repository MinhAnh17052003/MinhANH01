import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class AntiVirusGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('AtariBals AntiVirus')
        self.setGeometry(100, 100, 800, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Sidebar
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: #4169E1;")
        sidebar_layout = QVBoxLayout(sidebar)
        
        sidebar_buttons = ["Status", "Updates", "Settings", "Share Feedback", "Buy Premium", "Help"]
        for button_text in sidebar_buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("color: white; text-align: left; padding: 10px;")
            sidebar_layout.addWidget(button)
        
        scan_now_button = QPushButton("Scan Now")
        scan_now_button.setStyleSheet("background-color: #32CD32; color: white;")
        sidebar_layout.addWidget(scan_now_button)
        sidebar_layout.addStretch()

        main_layout.addWidget(sidebar, 1)

        # Main content area
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)

        title = QLabel("Scan")
        title.setFont(QFont("Arial", 20))
        content_layout.addWidget(title)

        subtitle = QLabel("Premium will be free forever. You just need to click button")
        content_layout.addWidget(subtitle)

        buttons_layout = QHBoxLayout()
        buttons = ["Quick Scan", "Web Protection", "Quarantine", "Full Scan", "Simple Update"]
        for button_text in buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("background-color: #FF1493; color: white;")
            buttons_layout.addWidget(button)
        
        content_layout.addLayout(buttons_layout)
        content_layout.addStretch()

        footer = QLabel("Get Premium to Enable: (Web Protection), (Full Scan), (Simple Update)")
        content_layout.addWidget(footer)

        main_layout.addWidget(content_area, 3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiVirusGUI()
    ex.show()
    sys.exit(app.exec_())