from flet import *
from flet import icons, colors


from .addproductpage import AddProduct

class DashBoard(UserControl):

    def __init__(self):
        super().__init__()
        self.build()


    def mainPage(self,e):
        self.column.current.controls = [Text("Anasayfa")]
        self.update()
    
    def change(self,e):
        index = e.control.selected_index
        if index == 0:
            self.column.current.controls = [AddProduct()]
        elif index == 1:
            self.column.current.controls = [Text("Stok Ekle")]
        elif index == 2:
            self.column.current.controls = [Text("Stok Görüntüle")]
        elif index == 3:
            self.column.current.controls = [Text("Ürün Görüntüle")]
        elif index == 4:
            self.column.current.controls = [Text("Stok Sil")]
        elif index == 5:
            self.column.current.controls = [Text("Çıkış Yap")]            
        self.update()


    def build(self):
        self.column = Ref[Column]()
        self.expand = True
        return Row(
            controls=[
                NavigationRail(
                    selected_index=0,
                    label_type="all",
                    min_width=100,
                    min_extended_width=400,
                    leading=FloatingActionButton(icon=icons.HOME, text="Anasayfa", on_click=self.mainPage),
                    group_alignment=-0.9,
                    destinations=[
                        NavigationRailDestination(
                            icon_content=Icon(icons.ADD_OUTLINED), 
                            selected_icon_content=Icon(icons.ADD), 
                            label="Ürün Ekle"
                        ),
                        NavigationRailDestination(
                            icon_content=Icon(icons.ADD_OUTLINED),
                            selected_icon_content=Icon(icons.ADD),
                            label="Stok Ekle",
                        ),
                        NavigationRailDestination(
                            icon_content=Icon(icons.SAVED_SEARCH_OUTLINED),
                            selected_icon_content=Icon(icons.SAVED_SEARCH),
                            label = "Stok Görüntüle",
                        ),
                        NavigationRailDestination(
                            icon_content=Icon(icons.SAVED_SEARCH_OUTLINED),
                            selected_icon_content=Icon(icons.SAVED_SEARCH),
                            label = "Ürün Görüntüle",
                        ),
                        NavigationRailDestination(
                            icon_content=Icon(icons.DELETE_OUTLINED),
                            selected_icon_content=Icon(icons.DELETE),
                            label="Stok Sil",
                        ),
                        NavigationRailDestination(
                            icon=icons.LOGOUT,
                            label="Çıkış Yap",
                        ),
                    ],
                    on_change=self.change,
                ),
                VerticalDivider(width=1),
                Column(
                    controls=[
                        Text("Anasayfa")
                    ],
                    horizontal_alignment="center",
                    ref=self.column
                )
            ],
            expand=True,
        )

        