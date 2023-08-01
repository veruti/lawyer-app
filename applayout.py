from flet import Column, Control, CrossAxisAlignment, IconButton, MainAxisAlignment, Page, Row, Text, colors, icons

from sidebar import LayerAppSidebar


class AppLayout(Row):
    def __init__(self, page: Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page

        self.toggle_button = IconButton(
            icon=icons.ARROW_CIRCLE_LEFT,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
        )
        self.sidebar = LayerAppSidebar(self, page)
        self._active_view: Control = Column(
            controls=[Text("Active View")],
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
        )

        self.controls = [self.sidebar, self.toggle_button, self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_nav_rail(self, _):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_button.selected = not self.toggle_button.selected
        self.page.update()
