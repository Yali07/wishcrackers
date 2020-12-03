from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("./firstscreen/firstscreen.kv")

class FirstScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    def prime_video(self):
        self.parent.ids.second_screen.player.state = 'play'
