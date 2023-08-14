from PyQt6.QtWidgets import QTabWidget

from src.gui.add_data.tab_bar_widget import AddDataTab
from src.gui.show_table_view.table_view import ShowTableView


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
            ("Добавить данные", AddDataTab()),
            ("Посмотреть данные", ShowTableView()),
        ]:
            self.addTab(tab, tab_name)
