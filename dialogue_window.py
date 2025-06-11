import sys
import ollama
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QHBoxLayout, QTextEdit, QLineEdit, QPushButton
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

try:
    from qt_material import apply_stylesheet
    QT_MATERIAL_AVAILABLE = True
except ImportError:
    QT_MATERIAL_AVAILABLE = False

class ChatWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle("Задание №2")
        self.setGeometry(100, 100, 700, 600)

        self.model_name = 'dolphin-llama3' 
        
        # history
        self.messages = []

        # creating interface + applying settings
        self.init_ui()
        self.apply_styles()

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

    def apply_styles(self):
        font = QFont("Arial", 12)
        self.chat_display.setFont(font)
        self.input_field.setFont(font)
        self.send_button.setFont(font)

        if QT_MATERIAL_AVAILABLE:
            apply_stylesheet(app, theme='dark_teal.xml')
        else:
            # if GM style does not exists
            self.setStyleSheet("""
                QMainWindow { background-color: #2b2b2b; }
                QTextEdit { background-color: #3c3f41; color: #a9b7c6; border-radius: 5px; }
                QLineEdit { background-color: #3c3f41; color: #a9b7c6; border-radius: 5px; padding: 5px; }
                QPushButton { background-color: #007bff; color: white; border: none; padding: 8px; border-radius: 5px; }
                QPushButton:hover { background-color: #0056b3; }
            """)

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

        try:
            # history block
            response = ollama.chat(model=self.model_name, messages=self.messages)
            assistant_reply = response["message"]["content"]
            
            self.messages.append({"role": "assistant", "content": assistant_reply})

            self.chat_display.append(f"\n[Модель]: {assistant_reply}\n")

        except Exception as e:
            error_message = (f"\n[ERROR]: не получилось подключиться к ollama {e}")
            self.chat_display.append(error_message)
            self.messages.pop()
        
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())