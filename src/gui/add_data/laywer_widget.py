from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QWidget

from src.storage.storage import LawyerData, repo


class AddLawyerWidget(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.last_name_layout = PropertyLayout("Фамилия")
        self.first_name_layout = PropertyLayout("Имя")
        self.middle_name_layout = PropertyLayout("Отчетсво")
        self.agree_button = AgreeButton(self)

        self._grid = QGridLayout()

        self._grid.addWidget(self.last_name_layout.label, 0, 0)
        self._grid.addWidget(self.last_name_layout.line_edit, 0, 1)

        self._grid.addWidget(self.first_name_layout.label, 1, 0)
        self._grid.addWidget(self.first_name_layout.line_edit, 1, 1)

        self._grid.addWidget(self.middle_name_layout.label, 2, 0)
        self._grid.addWidget(self.middle_name_layout.line_edit, 2, 1)

        self._grid.addWidget(self.agree_button, 3, 2)

        self.setLayout(self._grid)

    def get_lawyer_data(self) -> LawyerData:
        last_name = self.last_name_layout.line_edit.text()
        middle_name = self.middle_name_layout.line_edit.text()
        first_name = self.first_name_layout.line_edit.text()

        return LawyerData(
            last_name=last_name,
            middle_name=middle_name,
            first_name=first_name,
        )


class PropertyLayout:
    def __init__(self, param_name: str):
        self.label = QLabel(text=f"{param_name}")
        self.line_edit = QLineEdit()
        self._set_properties()

    def _set_properties(self):
        self.line_edit.setMaxLength(30)


class AgreeButton(QPushButton):
    def __init__(self, main_widget: AddLawyerWidget, *args, **kwargs) -> None:
        self._main_widget = main_widget
        super().__init__(text="Сохранить", *args, **kwargs)

        self.clicked.connect(self.keyPressEvent)

    def keyPressEvent(self):
        lawyer = self._main_widget.get_lawyer_data()
        repo.add(lawyer=lawyer)
