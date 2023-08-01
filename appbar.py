from flet import AppBar, IconButton, Page, PopupMenuButton, PopupMenuItem, Text, icons


class LayerAppBar(AppBar):
    def __init__(self, page: Page, *args, **kwargs):
        self.help_button = HelpButton()
        self.menu_button = MenuButton(page)

        super().__init__(
            title=Text("Юрист"),
            actions=[self.help_button, self.menu_button],
            *args,
            **kwargs,
        )


class HelpButton(IconButton):
    def __init__(self, *args, **kwargs):
        super().__init__(icon=icons.HELP, *args, **kwargs)


class MenuButton(PopupMenuButton):
    def __init__(self, page: Page, *args, **kwargs):
        self.menu_items = [
            PopupMenuItem(text="Settings"),
            PopupMenuItem(text="Exit", on_click=lambda _: page.window_close()),
        ]

        super().__init__(items=self.menu_items, *args, **kwargs)
