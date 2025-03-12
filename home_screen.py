import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt
from encrypt_screen import EncryptScreen
from decrypt_screen import DecryptScreen

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Encryption Tool")
        self.setGeometry(100, 100, 500, 350)

        #dark theme with neon accents
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
            QLabel {
                font-size: 14px;
                color: #B0B0B0;
            }
        """)

        layout = QVBoxLayout()

        title = QLabel("🔒 Secure Your Files")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.encrypt_button = QPushButton("Encrypt a File")
        self.encrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encrypt_button.clicked.connect(self.open_encrypt_screen)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton("Decrypt a File")
        self.decrypt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decrypt_button.clicked.connect(self.open_decrypt_screen)
        layout.addWidget(self.decrypt_button)

        footer = QLabel('Developed with ❤️ by <a href="https://github.com/Tharunya07">@Tharunya07</a>')
        footer.setOpenExternalLinks(True)
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)

        self.setLayout(layout)

    def open_encrypt_screen(self):
        self.encrypt_screen = EncryptScreen()
        self.encrypt_screen.show()

    def open_decrypt_screen(self):
        self.decrypt_screen = DecryptScreen()
        self.decrypt_screen.show()

# Main entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeScreen()
    home.show()
    sys.exit(app.exec_())
