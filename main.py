import flet as ft
from flet import Page

from src.app import LawyerApp


def main(page: Page):
    page.padding = 0
    page.fonts = {"Pacifico": "/Pacifico-Regular.ttf"}
    page.bgcolor = ft.colors.BLUE_GREY_200
    page.update()
    LawyerApp(page)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
