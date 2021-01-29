from main_imports import MDCard, MDLabel, MDScreen, MDSeparator
from libs.applibs import utils
import chatMain
utils.load_kv("chat_room.kv")

class Chat_Room_Screen(MDScreen):
    def on_enter(self, *args):

        self.getilkMesaj("Selam ben Hasbi size nasıl yardımcı olabilirim. Bana istediğinizi sorabilirsiniz.")

    def chat_textbox(self):
        """
            MDCard size change when MSGbox use multilines.
            MDCard y axis size incress when MSGbox y axis size incress
        """
        fixed_Y_size = self.ids.root_chatroom.size[1]/3
        msg_textbox=self.ids.msg_textbox.size

        if msg_textbox[1] <= fixed_Y_size:
            
            self.ids.send_card.size[1]=msg_textbox[1]
            #print(msg_textbox)
        else:
            self.ids.send_card.size[1]=fixed_Y_size


    def send_msg(self, msg_data):
        """
            When send button use to send msg this function call
            and clear MSGbox
        """

        text_msg = MDLabel(text=msg_data, halign="left")
        self.adds_widget(text_msg,"Sen","Secondary")
        self.get_msg(msg_data)

        # ->> sizeY is equal to msg_textbox sizeY because text_msg sizeY not work
        # that's why i use msg_textbox is called 'Jugaad'
    def adds_widget(self, text_msg,isim,renk,yon="left",uzunluk =60):
        sizeX = self.ids.msg_textbox.size[0]

        sizeY = self.ids.msg_textbox.size[1] + uzunluk
        msg_card = MDCard(
            orientation="vertical",
            size_hint=[None, None],
            size=[sizeX, sizeY],
            spacing=8,
            padding=20,
            elevation=9,
            ripple_behavior=True,
            radius=[25, 25, 25, 0],


        )
        msg_card.add_widget(MDLabel(
            text=isim,
            theme_text_color=renk,
            halign=yon,
            size_hint_y=None,
            height=50,

        ))
        msg_card.add_widget(MDSeparator(
            height="1dp"
        ))

        msg_card.add_widget(text_msg)
        self.ids.all_msgs.add_widget(msg_card)

        self.ids.msg_scroll_view.scroll_to(msg_card)
        self.ids.msg_textbox.text = ""


    def get_msg(self, msg_data):
        """
            When send button use to send msg this function call
            and clear MSGbox
        """
        cevap =chatMain.chat(msg_data)[0]
        uzunluk = len(cevap)/2
        if uzunluk < 60:
            uzunluk = 60
        text_msg = MDLabel(text=cevap,
                           halign="right",
                           theme_text_color= "Custom",
                           text_color=(0,0,1,1)
        )

        self.adds_widget(text_msg,"Hasbi","Error","right",uzunluk)

    def getilkMesaj(self,msg_data):
        cevap = msg_data
        uzunluk = len(cevap) / 2
        if uzunluk < 60:
            uzunluk = 60
        text_msg = MDLabel(text=cevap,
                           halign="right",
                           theme_text_color="Custom",
                           text_color=(0, 0, 1, 1)
                           )

        self.adds_widget(text_msg, "Hasbi", "Error", "right", uzunluk)


