import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QTextEdit, QLineEdit, QPushButton
)
from PyQt6.QtCore import Qt

class ChatWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle("Задание №2")
        self.setGeometry(100, 100, 700, 600)
        
        # history
        self.messages = []

        # creating interface
        self.init_ui()

    def init_ui(self):
        
        # init
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        # input label
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Введите сообщение")
        
        # send
        self.input_field.returnPressed.connect(self.chat)

        # send label
        self.send_button = QPushButton("Отправить")
        self.send_button.clicked.connect(self.chat)

        # style line
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)

        # style layer
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_display)
        main_layout.addLayout(input_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def chat(self):
        
        # MAIN CHAT
        user_input = self.input_field.text().strip()
        if not user_input:
            return

        # +history
        self.messages.append({"role": "user", "content": user_input})

        # showing message
        self.chat_display.append(f"[Пользователь]: {user_input}")
        self.input_field.clear()
        
        # update 
        QApplication.processEvents()

        # временно
        self.chat_display.append(f"\n in progress \n")
        
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())