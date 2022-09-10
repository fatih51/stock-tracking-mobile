from flet import *
from flet import icons

import requests
import globaldata

class Login(UserControl):
    def login(self, e):
        email = self.email.current.value
        password = self.password.current.value
        user = {
            "email": email,
            "password": password
        }
        if email == "" or password == "":
            self.text.current.value = "Lütfen tüm alanları doldurunuz."
            self.text.current.color = "red"
            self.update()
        else:
            loginReq=requests.post(globaldata.server+"/login", json=user)
            if loginReq.status_code == 200:
                self.text.current.value = "Giriş başarılı"
                self.text.current.color = "green"
                self.update()
                globaldata.token = loginReq.cookies.get("token")
                time.sleep(1)
                self.page.go("/dashboard")
            else:
                self.text.current.value = "Giriş başarısız, verileri kontrol ediniz."
                self.text.current.color = "red"
                self.update()

    def build(self):
        self.expand = True
        self.email = Ref[TextField]()
        self.password = Ref[TextField]()
        self.text = Ref[Text]()
        return Column(
            controls=[
                Text("Giriş Yap",ref=self.text,size=25),
                TextField(label="E-Mail", icon=icons.EMAIL, width=700, ref=self.email),
                TextField(label="Şifre", password=True, can_reveal_password=True, icon=icons.PASSWORD_SHARP, width=700, ref=self.password),
                Row(
                    controls=[
                        ElevatedButton(text="Giriş Yap", icon=icons.LOGIN, on_click=self.login),
                        TextButton(text="Hesabın mı yok? Kaydol", icon=icons.APP_REGISTRATION, on_click=lambda _: self.page.go("/register"))
                    ],
                    alignment="center",
                )
            ],
            horizontal_alignment="center",
            alignment="center",
        )