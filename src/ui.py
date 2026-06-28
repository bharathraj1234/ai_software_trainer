
from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect,QScrollArea,QSizePolicy
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QColor, QFont
from backend import gemma_call
from math import sqrt

class AITrainer(QWidget):
    def __init__(self):
        super().__init__()
        self.drag_position = QPoint()
        self.setup_window()
        self.create_widgets()
        self.create_layout()
        self.apply_style()

    def setup_window(self):
        self.setWindowTitle("AI Software Trainer")
        self.resize(500,580)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def create_widgets(self):
        self.card=QFrame()
        self.card.setObjectName("card")
        shadow=QGraphicsDropShadowEffect()
        shadow.setBlurRadius(45)
        shadow.setOffset(0,8)
        shadow.setColor(QColor(0,0,0,170))
        self.card.setGraphicsEffect(shadow)
        self.title=QLabel("AI Software Trainer")
        self.title.setFont(QFont("Segoe UI",13,QFont.Weight.Bold))
        self.status=QLabel("Ready")
        self.close_button=QPushButton("✕")
        self.close_button.setFixedSize(32,32)
        self.close_button.clicked.connect(self.close)
        self.chat=QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setPlaceholderText("Conversation will appear here...")
        self.input=QLineEdit()
        self.input.setPlaceholderText("Ask anything...")
        self.send_button=QPushButton("➜")
        self.send_button.setFixedSize(55,45)
        self.send_button.clicked.connect(self.send_message)
        self.input.returnPressed.connect(self.send_message)

    def create_layout(self):
        outer=QVBoxLayout(self)
        outer.setContentsMargins(15,15,15,15)
        outer.addWidget(self.card)
        card_layout=QVBoxLayout(self.card)
        card_layout.setContentsMargins(20,20,20,20)
        card_layout.setSpacing(15)
        header=QHBoxLayout()
        header.addWidget(self.title)
        header.addStretch()
        header.addWidget(self.close_button)
        bottom=QHBoxLayout()
        bottom.addWidget(self.input)
        bottom.addWidget(self.send_button)
        card_layout.addLayout(header)
        card_layout.addWidget(self.status)
        card_layout.addWidget(self.chat)
        card_layout.addLayout(bottom)

    def apply_style(self):
        self.setStyleSheet('''
        QWidget{background:transparent;}
        #card{background:#2B2D31;border-radius:28px;border:1px solid rgba(255,255,255,18);}
        QLabel{color:#F4F4F4;background:transparent;font-size:14px;}
        QTextEdit{background:#202225;color:#ECECEC;border:none;border-radius:16px;padding:12px;font-size:14px;}
        QLineEdit{background:#1C1D21;color:white;border:1px solid rgba(255,255,255,20);border-radius:18px;padding:12px;font-size:14px;}
        QLineEdit::placeholder{color:#7D7D7D;}
        QPushButton{background:#5865F2;color:white;border:none;border-radius:16px;font-size:15px;font-weight:bold;}
        QPushButton:hover{background:#6F7BFF;}
        QPushButton:pressed{background:#4652D9;}
        ''')

    def mousePressEvent(self,event):
        if event.button()==Qt.MouseButton.LeftButton:
            self.drag_position=event.globalPosition().toPoint()-self.frameGeometry().topLeft()

    def mouseMoveEvent(self,event):
        if event.buttons()==Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint()-self.drag_position)

    def send_message(self):
        prompt = self.input.text()
        # self.chat.append(f"You: {prompt}") # instead for this we use below for being in the right side
        self.chat.append(f"""
            <div align="right">
            <span style="
            background:#5865F2;
            color:white;
            padding:8px 12px;
            border-radius:10px;
            ">
            {prompt}
            </span>
            </div>
            """)
        QApplication.processEvents()
        answer = gemma_call(prompt)
        # self.chat.append(f"AI: {answer}")  # same for this also
        self.chat.append(f"""
            <div align="left">
            <span style="
            background:#3A3C42;
            color:white;
            padding:8px 12px;
            border-radius:10px;
            ">
            {answer}
            </span>
            </div>
            """)
        self.input.clear()
        print(answer)

    

if __name__=="__main__":
    app=QApplication([])
    window=AITrainer()
    window.show()
    app.exec()