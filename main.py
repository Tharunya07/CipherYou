import sys
from PyQt5.QtWidgets import QApplication
from home_screen import HomeScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = HomeScreen()
    home.show()
    sys.exit(app.exec_())
