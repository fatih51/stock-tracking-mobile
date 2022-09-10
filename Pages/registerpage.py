from flet import *
from flet import icons

import time

import globaldata

import requests

class Register(UserControl):

    def register(self, e):
        name = self.name.current.value
        email = self.email.current.value
        password = self.password.current.value
        user = {
            "name": name,
            "email": email,
            "password": password
        }
        if name == "" or email == "" or password == "":
            self.text.current.value = "Lütfen tüm alanları doldurun"
            self.text.current.color = "red"
            self.update()
        else:
            registerReq = requests.post(globaldata.server+"/register", json=user)
            if registerReq.status_code == 200:
                self.text.current.value = "Kayıt başarılı"
                self.text.current.color = "green"
                self.update()
                time.sleep(1.2)
                self.page.go("/login")
            else:
                self.text.current.value = "Kayıt başarısız"
                self.text.current.color = "red"
                self.update()

    def build(self):
        self.expand = True
        self.name = Ref[TextField]()
        self.email = Ref[TextField]()
        self.password = Ref[TextField]()
        self.text = Ref[Text]()
        return Column(
            controls=[
                Text("Kayıt Ol",ref=self.text,size=25),
                TextField(label="İsim", icon=icons.PERSON, width=700, ref=self.name),
                TextField(label="E-Mail", icon=icons.EMAIL, width=700, ref=self.email),
                TextField(label="Şifre", password=True, can_reveal_password=True, icon=icons.PASSWORD_SHARP, width=700, ref=self.password),
                Row(
                    controls=[
                        ElevatedButton(text="Kaydol ol", icon=icons.APP_REGISTRATION_ROUNDED, on_click=self.register ),
                        TextButton(text="Hesabın varsa\nGiriş Yap", icon=icons.LOGIN_OUTLINED, on_click=lambda _: self.page.go("/login"))
                    ],
                    alignment="center",
                    spacing=50
                )
            ],
            horizontal_alignment="center",
            alignment="center",
        )