from flet import CrossAxisAlignment, IconButton, MainAxisAlignment, Page, Row, Text, icons

from src.sidebar import LayerAppSidebar


class AppLayout(Row):
    def __init__(self, page: Page, *args, **kwargs):
        self.page = page
        self._views = [
            Text("Active View 1"),
            Text("Active View 2"),
            Text("Active View 3"),
            Text("Active View 4"),
        ]
        for view in self._views:
            view.visible = False

        self._sidebar = LayerAppSidebar(page, self._views)
        self._toggle_button = ToggleButton(page, self)

        super().__init__(
            controls=[self._sidebar, self._toggle_button, *self._views],
            alignment=MainAxisAlignment.START,
            vertical_alignment=CrossAxisAlignment.START,
            height=page.window_height,
            width=page.window_height,
            *args,
            **kwargs
        )


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
        self.app_layout._sidebar.visible = not self.app_layout._sidebar.visible
        self.app_layout._toggle_button.selected = not self.app_layout._toggle_button.selected
        self.page.update()
