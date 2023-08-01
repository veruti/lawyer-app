from flet import (
    Divider,
    Icon,
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    Row,
    Text,
    colors,
    icons,
)


class LayerAppSidebar(NavigationRail):
    def __init__(self, *args, **kwargs):
        self.report_bar = ReportBar()
        self.table_cange_bar = TableChangeBar()
        self.table_bar = TableBar()
        self.settings_bar = SettingBar()

        self.destinations = [
            self.report_bar,
            self.table_bar,
            self.table_cange_bar,
            self.settings_bar,
        ]

        super().__init__(
            destinations=self.destinations,
            height=500,
            selected_index=0,
            extended=True,
            min_width=100,
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
            *args,
            **kwargs,
        )

        self.top_nav_rail = NavigationRail(
            selected_index=None,
            on_change=self.top_nav_change,
            destinations=self.destinations,
            bgcolor=colors.BLUE_GREY,
            extended=True,
            expand=True,
        )

    def top_nav_change(self, e):
        self.top_nav_rail.selected_index = e.control.selected_index
        self.update()


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
