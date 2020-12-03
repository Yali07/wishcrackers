from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.video import Video
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

Builder.load_file("./secondscreen/secondscreen.kv")

class SecondScreen(Screen):
   
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.player = Video(source='./Video/crackers.mp4')
        self.player.state = 'stop'
        self.player.size_hint =[1,1]
        self.player.allow_stretch = True
        self.player.allow_fullscreen = True
        self.add_widget(self.player)
        with self.canvas.before:
            Color(0,0,0)
            Rectangle(size=(2000,2000),pos=self.pos)
    def label_anim(self):
        wish_lbl_anim  = Animation(d=11)
        wish_lbl_anim += Animation(opacity=1) 
        wish_lbl_anim += Animation(d=5) 
        wish_lbl_anim += Animation(opacity=0)
        name_lbl_anim  = Animation(d=11)
        name_lbl_anim += Animation(opacity=1) 
        name_lbl_anim += Animation(d=5) 
        name_lbl_anim += Animation(opacity=0)
        wish_lbl_anim.start(self.ids.wish_label)
        name_lbl_anim.start(self.ids.name_label)
    def video_end_dialogbox(self,*args):
        self.ids.video_end.opacity = 1
    def delay_dialogbox(self,*args):
        Clock.schedule_once(self.video_end_dialogbox,38/2)
    def erase_video_end_dialogbox(self,*args):
        self.ids.video_end.opacity = 0
        
        
        
    