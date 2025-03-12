import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from encryption_logic import EncryptionLogic

class DecryptScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.attempts = 4

    def init_ui(self):
        self.setWindowTitle("🔓 Decrypt a File")
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

        self.label = QLabel("🔍 Select a file to decrypt")
        self.label.setFont(QFont("Arial", 14))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.select_button = QPushButton("📂 Select File")
        self.select_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("🔑 Enter password for decryption")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.decrypt_button = QPushButton("🔓 Decrypt")
        self.decrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decrypt_button.clicked.connect(self.decrypt_file)
        layout.addWidget(self.decrypt_button)

        self.setLayout(layout)

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select File to Decrypt")

        if file_path:
            if not file_path.endswith(".enc"):
                QMessageBox.warning(self, "⚠️ Error", "This file is not encrypted.")
            else:
                self.file_path = file_path
                self.label.setText(f"✅ Selected: {os.path.basename(file_path)}")

    def decrypt_file(self):
        if not hasattr(self, 'file_path'):
            QMessageBox.warning(self, "⚠️ Error", "Please select a file.")
            return

        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "⚠️ Error", "Please enter a password.")
            return

        result = EncryptionLogic.decrypt_file(self.file_path, password)
        if not result.startswith("Error"):
            QMessageBox.information(self, "✅ Success", "File decrypted successfully!")
            self.close() 
        else:
            self.attempts -= 1
            if self.attempts > 0:
                QMessageBox.warning(self, "⚠️ Incorrect Password", f"Wrong password! {self.attempts} attempts remaining.")
            else:
                QMessageBox.critical(self, "❌ Too Many Attempts", "Too many failed attempts. Closing decryption window.")
                self.close() 
