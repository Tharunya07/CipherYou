import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from encryption_logic import EncryptionLogic

class EncryptScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("🔐 Encrypt a File")
        self.setGeometry(100, 100, 500, 300)
        self.setStyleSheet("""
            QWidget {
                background-color: #0D0D0D;
                color: #00FFD1;
            }
            QPushButton {
                background-color: #242424;
                color: #00FFD1;
                border: 2px solid #00FFD1;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #00FFD1;
                color: #0D0D0D;
                font-weight: bold;
                transform: scale(1.1);
            }
            QLineEdit {
                border: 2px solid #00FFD1;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout()

        self.label = QLabel("🔍 Select a file to encrypt")
        self.label.setFont(QFont("Arial", 14))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.select_button = QPushButton("📂 Select File")
        self.select_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("🔑 Enter password for encryption")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.encrypt_button = QPushButton("🔒 Encrypt")
        self.encrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encrypt_button.clicked.connect(self.encrypt_file)
        layout.addWidget(self.encrypt_button)

        self.setLayout(layout)

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File to Encrypt")

        if file_path:
            if file_path.endswith(".enc"):
                QMessageBox.warning(self, "⚠️ Error", "This file is already encrypted.")
            else:
                self.file_path = file_path
                self.label.setText(f"✅ Selected: {os.path.basename(file_path)}")

    def encrypt_file(self):
        if not hasattr(self, 'file_path'):
            QMessageBox.warning(self, "⚠️ Error", "Please select a file.")
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "⚠️ Error", "Please enter a password.")
            return

        result = EncryptionLogic.encrypt_file(self.file_path, password)
        if result.endswith(".enc"):
            QMessageBox.information(self, "✅ Success", "File encrypted successfully!")
            self.close() 
        else:
            QMessageBox.warning(self, "⚠️ Error", result)
