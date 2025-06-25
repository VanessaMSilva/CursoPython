from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from typing import Optional


class MainWindow(QMainWindow):
    def __init__(self, parent: Optional[QWidget] = None, *args, **kwargs) -> None: #type:ignore
        super().__init__(parent, *args, **kwargs)
        
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        # Exemplo de conteúdo:
        self.v_layout.addWidget(QLabel("Olá, mundo!"))
        #Definir icone
        
        
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
        self.adjustFixedSize()