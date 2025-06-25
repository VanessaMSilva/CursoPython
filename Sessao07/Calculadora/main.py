import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QVBoxLayout, QLabel
from src.main_window import MainWindow
from PySide6.QtGui import QIcon
from src.variables import WINDOW_ICON_PATH
from src.display import Display

def temp_label(text):
    label = QLabel(text)
    return label

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    #Display
    display = Display()
    window.addWidgetToVLayout(display)

    window.addWidgetToVLayout(temp_label('ola mundo'))

    window.show()
    app.exec()
