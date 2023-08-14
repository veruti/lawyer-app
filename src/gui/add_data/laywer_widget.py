from PyQt6.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QWidget


class AddLawyerWidget(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setLayout(AddLawyerLayout())


class AddLawyerLayout(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super(QGridLayout, self).__init__(*args, **kwargs)

        self._first_name_layout = PropertyLayout("Имя")
        self._last_name_layout = PropertyLayout("Фамилия")

        self._agree_button = AgreeButton()

        self.addWidget(self._first_name_layout.label, 0, 0)
        self.addWidget(self._first_name_layout.line_edit, 0, 1)

        self.addWidget(self._last_name_layout.label, 1, 0)
        self.addWidget(self._last_name_layout.line_edit, 1, 1)

        self.addWidget(self._agree_button, 2, 2)


class AgreeButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(text="Сохранить", *args, **kwargs)


class PropertyLayout:
    def __init__(self, param_name: str):
        self.label = QLabel(text=f"{param_name}")
        self.line_edit = QLineEdit()
        self._set_properties()

    def _set_properties(self):
        self.line_edit.setMaxLength(30)
