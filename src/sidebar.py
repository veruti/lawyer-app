from flet import Icon, NavigationRail, NavigationRailDestination, Page, Text, icons


class LayerAppSidebar(NavigationRail):
    def __init__(self, page: Page, views, *args, **kwargs):
        self.page = page

        self.report_bar = ReportBar()
        self.table_cange_bar = TableChangeBar()
        self.table_bar = TableBar()
        self.settings_bar = SettingBar()

        self._views = views

        self.destinations = [
            self.report_bar,
            self.table_bar,
            self.table_cange_bar,
            self.settings_bar,
        ]

        super().__init__(
            destinations=self.destinations,
            selected_index=0,
            on_change=lambda e: self._on_change(e, self),
            *args,
            **kwargs,
        )

    @staticmethod
    def _on_change(e, self):
        print("Selected destination:", e.control.selected_index)
        for i in self._views:
            i.visible = False

        self._views[e.control.selected_index].visible = True
        self.page.update()


class ReportBar(NavigationRailDestination):
    def __init__(self, *args, **kwargs):
        super().__init__(
            selected_icon_content=Icon(icons.EDIT_DOCUMENT),
            label_content=Text("Написать отчёт"),
            icon_content=Icon(icons.ALARM),
            *args,
            **kwargs,
        )


class TableChangeBar(NavigationRailDestination):
    def __init__(self, *args, **kwargs):
        super().__init__(
            icon_content=Icon(icons.CHANGE_CIRCLE),
            label_content=Text("Дополнить данные"),
            *args,
            **kwargs,
        )


class TableBar(NavigationRailDestination):
    def __init__(self, *args, **kwargs):
        super().__init__(
            selected_icon_content=Icon(icons.BOOKMARK),
            icon_content=Icon(icons.TABLE_VIEW),
            label_content=Text("Просмотреть данные"),
            *args,
            **kwargs,
        )


class SettingBar(NavigationRailDestination):
    def __init__(self, *args, **kwargs):
        super().__init__(
            icon=icons.SETTINGS_OUTLINED,
            selected_icon_content=Icon(icons.SETTINGS),
            label_content=Text("Настройки"),
            label="settings",
            *args,
            **kwargs,
        )
