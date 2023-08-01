import flet as ft
from flet import Page

from appbar import LayerAppBar
from applayout import AppLayout


class LayerApp:
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


def main(page: Page):
    # page.padding = 0
    # page.fonts = {"Pacifico": "/Pacifico-Regular.ttf"}
    # page.bgcolor = ft.colors.BLUE_GREY_200
    # page.update()
    LayerApp(page)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
