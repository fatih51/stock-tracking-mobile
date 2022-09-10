from flet import *
from flet import icons

class HomePage(UserControl):
    def build(self):
        self.expand = True
        return Column(
            controls=[
                Row(
                    controls=[
                        TextButton(text="Hesabın mı yok? Kaydol", icon=icons.APP_REGISTRATION_SHARP, on_click=lambda _: self.page.go("/register")),
                        TextButton(text="Hesabın varsa\nGiriş Yap", icon=icons.LOGIN_OUTLINED, on_click=lambda _: self.page.go("/login")),
                    ],
                    spacing=50,
                    alignment="center",
                )
            ],
            horizontal_alignment="center",
            alignment="center",
        )