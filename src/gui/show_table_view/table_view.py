from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QTabWidget


class ShowTableView(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_tabs()

    def _init_tabs(self):
        self.addTab(ShowTable(5, 2), "Добавить юриста")


class ShowTable(QTableWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setHorizontalHeaderLabels(["Имя", "Фамилия"])

        self.setItem(0, 0, QTableWidgetItem("Максим"))
        self.setItem(0, 1, QTableWidgetItem("Лепьявко"))
