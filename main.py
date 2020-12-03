from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window


class MainScreen(ScreenManager):
    
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.on_key)
        
#Esc key
    def on_key(self,window,key,*args):
        if key == 27:
            if self.current_screen.name == "first_screen":
                return False
            elif self.current_screen.name == "second_screen":
                self.ids.second_screen.player.state ='stop'
                self.current = "first_screen"
                self.ids.second_screen.erase_video_end_dialogbox()
                return True
            elif self.current_screen.name == "download_screen":
                self.current = "first_screen"
                self.ids.download_screen.close_dialog()
                return True

class MainApp(MDApp):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
    Window.clearcolor = (0,0,0,1)
    MainApp().run()