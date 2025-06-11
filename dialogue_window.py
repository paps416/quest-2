import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

class ChatWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle("Задание №2")
        self.setGeometry(100, 100, 700, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())