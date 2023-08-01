from flet import Column, Control, CrossAxisAlignment, IconButton, MainAxisAlignment, Page, Row, Text, icons

from sidebar import LayerAppSidebar


class AppLayout(Row):
    def __init__(self, page: Page, sidebar: LayerAppSidebar, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.sidebar = sidebar

        self.toggle_button = ToggleButton(page, self)
        self._active_view: Control = Column(
            controls=[Text("Active View")],
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.START,
        )

        self.controls = [self.sidebar, self.toggle_button, self.active_view]

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()


class ToggleButton(IconButton):
    def __init__(self, page: Page, app_layout: AppLayout, *args, **kwargs):
        self.page: Page = page
        self.app_layout: AppLayout = app_layout

        super().__init__(
            icon=icons.ARROW_CIRCLE_LEFT,
            selected=False,
            selected_icon=icons.ARROW_CIRCLE_RIGHT,
            on_click=self.toggle_nav_rail,
            *args,
            **kwargs
        )

    def toggle_nav_rail(self, _):
        self.app_layout.sidebar.visible = not self.app_layout.sidebar.visible
        self.app_layout.toggle_button.selected = not self.app_layout.toggle_button.selected
        self.page.update()
