import sys

from PyQt6.QtWidgets import QApplication

from src.gui.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
