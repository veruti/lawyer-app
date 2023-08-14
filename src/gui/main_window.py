from PyQt6.QtWidgets import QMainWindow

from src.gui.navigation_bar import NavigationBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._navigation_bar = NavigationBar()

        self.setWindowTitle("Lawyer")
        self._set_properties()

    def _set_properties(self):
        self.setCentralWidget(self._navigation_bar)
