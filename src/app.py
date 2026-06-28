from PyQt6.QtWidgets import QApplication
from ui import AITrainer
app = QApplication([])
from backend import gemma_call


window = AITrainer()

window.show()

        

app.exec()