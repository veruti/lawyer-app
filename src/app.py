from flet import Page

from src.appbar import LayerAppBar
from src.applayout import AppLayout


class LawyerApp:
    def __init__(self, page: Page):
        self.page = page
        self.page.on_keyboard_event = lambda e: self._close_app() if e.ctrl & (e.key == "Q") else ...

        self.appbar = LayerAppBar(self.page)

        self.layout = AppLayout(page)
        self.page.appbar = self.appbar
        self.page.add(self.layout)
        self.page.update()

    def _close_app(self):
        self.page.window_close()
