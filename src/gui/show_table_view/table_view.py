from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget

from src.storage.storage import repo


class ShowDataTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_tabs()

    def _init_tabs(self):
        self.addTab(ShowTable(), "Добавить юриста")


class ShowTable(QTableWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._columns = ["Фамилия", "Имя", "Отчество"]

        self.setRowCount(len(repo.get_all()))
        self.setColumnCount(len(self._columns))
        self.setHorizontalHeaderLabels(self._columns)

        for row, value in enumerate(repo.get_all()):
            self.setItem(row, 0, QTableWidgetItem(str(value.last_name)))
            self.setItem(row, 1, QTableWidgetItem(str(value.first_name)))
            self.setItem(row, 2, QTableWidgetItem(str(value.middle_name)))
