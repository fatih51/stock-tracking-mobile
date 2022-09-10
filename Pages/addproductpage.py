from flet import *
from flet import icons, colors

import globaldata

import requests

class AddProduct(UserControl):
    def __init__(self):
        super().__init__()
        self.build()
    
    def addProduct(self,e):
        productName = self.productName.current.value
        productDescription = self.productDescription.current.value
        productCategory = self.productCategory.current.value
        if productName == "" or productDescription == "" or productCategory == "":
            self.title.current.value = "Lütfen tüm alanları doldurunuz."
            self.title.current.color = colors.RED  
        else:
            try:
                productCategory = int(productCategory)
            except ValueError:
                pass
            if type(productCategory) == int:
                newProduct = {
                    "name": productName,
                    "description": productDescription,
                    "category": productCategory
                }
                productReq=requests.post(globaldata.server+"/newProduct", json=newProduct, headers={'Authorization': globaldata.token})
                if productReq.status_code == 202:
                    self.title.current.value = "Ürün Eklendi"
                    self.title.current.color = colors.GREEN
                    self.page.go("/dashboard")
                else:
                    self.title.current.value = "Ürün Eklenemedi"
                    self.title.current.color = colors.RED

            else:
                self.title.current.value = "Kategori ID sayı olmalıdır."
                self.title.current.color = colors.RED
        self.update()

    def build(self):
        self.expand = True
        self.productName = Ref[TextField]()
        self.productDescription = Ref[TextField]()
        self.productCategory = Ref[TextField]()
        self.title = Ref[Text]()
        return Column(
            controls=[
                Text("Ürün Ekle",size=30,ref=self.title),
                TextField(label="Ürün Adı", icon=icons.LABEL, width=700, ref=self.productName),
                TextField(label="Ürün Açıklaması", icon=icons.DESCRIPTION, width=700, ref=self.productDescription),
                TextField(label="Kategori ID",icon=icons.CATEGORY, width=700, ref=self.productCategory),
                Row(
                    controls=[
                        ElevatedButton(text="Ürün Ekle", icon=icons.APP_REGISTRATION_ROUNDED, on_click=self.addProduct)
                    ],
                    alignment="center",
                )
            ],
            horizontal_alignment="center",
            alignment="center",           
        )