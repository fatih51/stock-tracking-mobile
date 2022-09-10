import flet
from flet import *
from flet import theme, colors

from Pages.homepage import HomePage
from Pages.loginpage import Login
from Pages.registerpage import Register
from Pages.dashboardpage import DashBoard

import globaldata

LIGHT_SEED_COLOR = colors.LIGHT_BLUE_ACCENT


def main(page:Page):
    page.theme_mode = "light"
    page.theme = theme.Theme(color_scheme_seed=LIGHT_SEED_COLOR, use_material3=True)

    
    def route_change(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    HomePage()
                ],
            )
        )
        if page.route == "/register":
            page.views.append(
                View(
                    "/register",
                    [
                        Register()
                    ],
                )
            )

        if page.route == "/login":
            page.views.append(
                View(
                    "/login",
                    [
                        Login()
                    ],
                )
            )
        if globaldata.token =="":
            page.route = "/"
        else:
            if page.route == "/dashboard":
                page.views.append(
                View(
                    "/dashboard",
                    [
                        DashBoard()
                    ],
                )
            )


        page.update()

    page.on_route_change = route_change
    page.go(page.route)


flet.app(target=main)