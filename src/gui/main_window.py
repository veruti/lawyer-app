from typing import Optional

from PyQt6 import QtCore
from PyQt6.QtGui import QKeyEvent, QMouseEvent
from PyQt6.QtWidgets import QLineEdit, QMainWindow, QTabBar, QTabWidget


class AddDataTab(QTabWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_tabs()

    def _init_tabs(self):
        self.setTabBar(TabBar())

        self.addTab(TabBar(), "text 1")
        self.addTab(TabBar(), "text 2")


class TabBar(QTabBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._editor = QLineEdit(self)
        self._set_properties()

    def _set_properties(self):
        self.setMovable(True)
        self.setTabsClosable(True)

        self._editor.setWindowFlags(QtCore.Qt.WindowType.Popup)
        self._editor.setFocusProxy(self)
        self._editor.editingFinished.connect(self.handleEditingFinished)
        self._editor.installEventFilter(self)

    def eventFilter(self, widget: Optional[QtCore.QObject], event: Optional[QtCore.QEvent]) -> bool:
        if event and self._event_filter_condition(event):
            self._editor.hide()

        return QTabBar.eventFilter(self, widget, event)

    def _event_filter_condition(self, event: QtCore.QEvent):
        print(event)
        if isinstance(event, QMouseEvent):
            return self._is_mouse_clicked_outside_editor(event)
        elif isinstance(event, QKeyEvent):
            return self._is_pressed_escape(event)

        return False

    # TODO: FIX logic
    def _is_pressed_escape(self, event: QKeyEvent) -> bool:
        return False

    # TODO: FIX logic
    def _is_mouse_clicked_outside_editor(self, event: QMouseEvent) -> bool:
        return False

    def mouseDoubleClickEvent(self, event):
        index = self.tabAt(event.pos())
        if index >= 0:
            self.editTab(index)

    def editTab(self, index: int):
        rect = self.tabRect(index)
        self._editor.setFixedSize(rect.size())
        self._editor.move(self.parent().mapToGlobal(rect.topLeft()))
        self._editor.setText(self.tabText(index))
        if not self._editor.isVisible():
            self._editor.show()

    def handleEditingFinished(self):
        index = self.currentIndex()
        if index >= 0:
            self._editor.hide()
            self.setTabText(index, self._editor.text())


class Sidebar(QTabWidget):
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
        ]:
            self.addTab(tab, tab_name)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lawyer")
        self._sidebar = Sidebar()

        self.setCentralWidget(self._sidebar)
