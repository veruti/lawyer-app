from PyQt6.QtWidgets import QTabWidget

from src.gui.add_data.tab_bar_widget import AddDataTab


class NavigationBar(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._set_tabs()
        self._set_properties()

    def _set_properties(self):
        self.setTabPosition(QTabWidget.TabPosition.West)
        self.setMovable(True)

    def _set_tabs(self):
        for tab_name, tab in [
            ("Данные", AddDataTab()),
        ]:
            self.addTab(tab, tab_name)
