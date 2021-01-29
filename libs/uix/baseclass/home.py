from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.toast import toast
from main_imports import ImageLeftWidget, MDScreen, TwoLineAvatarListItem
from libs.applibs import utils

utils.load_kv("home.kv")

hurriyet =False
cnn  = False
class Content(MDBoxLayout):
    '''Custom content.'''


class Home_Screen(MDScreen):

    def callback(self, instance, value):
        toast(value)
        if value =="Hurriyet":
            hurriyet =True


    def search_account(self):
        """
        this method use when search button pressed search_field
        contain data in string that you want to search on hamster server
        """

        # for dummy search item [------
        """
        twolineW= TwoLineAvatarListItem(text=f"{search_field}",
            secondary_text=f"@{search_field}")

        twolineW.add_widget(ImageLeftWidget(source="assets//img//hamster_icon.png"))
        
        self.ids.search_items.add_widget(twolineW)
        """
        self.ids.search_items.remove_widget(self.ids.search_items)
        for i in range(10):
            oneLineitem = OneLineListItem(text="Haber İçeriği Haber İçeriğiHaber İçeriğiHaber İçeriğiHaber İçeriği\nHaber İçeriğiHaber İçeriği\nHaber İçeriğiHaber İçeriğiHaber İçeriği")
            oneLineitem = MDLabel(text="Haber İçeriği Haber İçeriğiHaber İçeriğiHaber İçeriğiHaber İçeriği\nHaber İçeriğiHaber İçeriği\nHaber İçeriğiHaber İçeriğiHaber İçeriği",
                                  valign= "center")
            self.ids.search_items.add_widget(
                MDExpansionPanel(
                    icon=f"assets//img//hamster_icon.png",
                    content=oneLineitem,
                    panel_cls=MDExpansionPanelOneLine(text="Haber Başlığı")  # panel class
                )
            )

        # #  ----- ] end dummy search
