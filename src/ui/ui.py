from PyQt6.QtWidgets import QApplication,QWidget,QFrame,QLabel,QPushButton,QLineEdit,QTextEdit,QVBoxLayout,QHBoxLayout,QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt,QPoint
from PyQt6.QtGui import QColor,QFont

class AITrainer(QWidget):
    def __init__(self):
        super().__init__()
        self.drag_position=QPoint()
        self.setWindowTitle("AI Software Trainer")
        self.resize(500,580)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        outer=QVBoxLayout(self); outer.setContentsMargins(15,15,15,15)
        card=QFrame(); card.setObjectName("card")
        sh=QGraphicsDropShadowEffect(); sh.setBlurRadius(45); sh.setOffset(0,8); sh.setColor(QColor(0,0,0,170)); card.setGraphicsEffect(sh)
        outer.addWidget(card)
        layout=QVBoxLayout(card); layout.setContentsMargins(20,20,20,20); layout.setSpacing(15)
        h=QHBoxLayout()
        t=QLabel("AI Software Trainer"); t.setFont(QFont("Segoe UI",13,QFont.Weight.Bold)); h.addWidget(t); h.addStretch()
        c=QPushButton("✕"); c.setFixedSize(32,32); c.clicked.connect(self.close); h.addWidget(c); layout.addLayout(h)
        s=QLabel("🟢 Ready"); s.setObjectName("status"); layout.addWidget(s)
        self.chat=QTextEdit(); self.chat.setReadOnly(True); self.chat.append("Welcome 👋\n\nThis is your AI Software Trainer."); layout.addWidget(self.chat)
        b=QHBoxLayout(); self.input=QLineEdit(); self.input.setPlaceholderText("Ask anything..."); send=QPushButton("➜"); send.setFixedSize(55,45); b.addWidget(self.input); b.addWidget(send); layout.addLayout(b)
        self.setStyleSheet("""
        QWidget{background:transparent;}
        #card{background:#2B2D31;border-radius:28px;border:1px solid rgba(255,255,255,20);}
        QLabel{color:#F2F2F2;background:transparent;font-size:14px;}
        #status{color:#A9B0B8;font-size:13px;}
        QTextEdit{background:#202225;color:#ECECEC;border:none;border-radius:18px;padding:15px;font-size:14px;}
        QLineEdit{background:#1C1D21;color:white;border:1px solid rgba(255,255,255,25);border-radius:18px;padding:12px;font-size:14px;}
        QLineEdit::placeholder{color:#808080;}
        QPushButton{background:#5865F2;color:white;border:none;border-radius:16px;font-size:16px;font-weight:bold;}
        QPushButton:hover{background:#6B77FF;}
        QPushButton:pressed{background:#4652D9;}
        """)
    def mousePressEvent(self,e):
        if e.button()==Qt.MouseButton.LeftButton:
            self.drag_position=e.globalPosition().toPoint()-self.frameGeometry().topLeft()
    def mouseMoveEvent(self,e):
        if e.buttons()==Qt.MouseButton.LeftButton:
            self.move(e.globalPosition().toPoint()-self.drag_position)

app=QApplication([])
w=AITrainer(); w.show()
app.exec()