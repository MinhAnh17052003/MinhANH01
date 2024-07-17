import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class FrameRecorder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Frame Recorder')
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #90EE90;")  # Light green background

        main_layout = QVBoxLayout()

        # Title
        title_label = QLabel('Frame Recorder')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Arial', 24))
        main_layout.addWidget(title_label)

        # FPS input
        fps_layout = QHBoxLayout()
        fps_label = QLabel('Create an')
        self.fps_input = QLineEdit()
        self.fps_input.setFixedWidth(50)
        self.fps_input.setToolTip('Enter frames per second (integer > 0)')
        fps_suffix = QLabel('fps video')
        fps_layout.addStretch()
        fps_layout.addWidget(fps_label)
        fps_layout.addWidget(self.fps_input)
        fps_layout.addWidget(fps_suffix)
        fps_layout.addStretch()
        main_layout.addLayout(fps_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.pause_recording)
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_recording)
        self.end_button = QPushButton('End')
        self.end_button.clicked.connect(self.end_recording)
        button_layout.addStretch()
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.end_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        # Status label
        self.status_label = QLabel('Recording Paused')
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addStretch()
        main_layout.addWidget(self.status_label)

        self.setLayout(main_layout)

    def start_recording(self):
        try:
            fps = int(self.fps_input.text())
            if fps <= 0:
                raise ValueError
            self.status_label.setText(f'Started Recording at {fps} fps')
        except ValueError:
            QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid FPS value (integer > 0).')

    def pause_recording(self):
        self.status_label.setText('Recording Paused')

    def end_recording(self):
        self.status_label.setText('Recording Ended')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FrameRecorder()
    ex.show()
    sys.exit(app.exec_())


























































