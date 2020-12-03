from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from moviepy import editor
from threading import Thread
from kivymd.uix.dialog import MDDialog
import random 

Builder.load_file("./downloadscreen/download_screen.kv")

class DownloadScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.button = MDFlatButton(text='OK',on_press= self.close_dialog)
        self.button.state = 'normal'
        self.dialog_box = MDDialog(title ='Download Complete',buttons=[self.button],size_hint = [.75,.5])
        self.dialog_box.auto_dismiss =False
    def start_download(self, *args):
        def count_it(num):
            if num == 100:
                self.dialog_box.open()
                return
            num += 1
            self.ids.count.text = str(num)+ "%"
            self.ids.progress.value = num
            if self.ids.cancel.state == 'down':
                self.ids.count.text = str(0) + "%"
                self.ids.progress.value = 0
            Clock.schedule_once(lambda dt: count_it(num), 1/3)
        Clock.schedule_once(lambda dt: count_it(0), 0)
    
        
    def movie(self,*args):
        def annotate(clip,txt,txt_color,fontsize,font = './Font/led_counter-7.ttf'):
            text_clip = editor.TextClip(txt,fontsize=fontsize,font=font,color= txt_color,kerning= 3)
            cvc = editor.CompositeVideoClip([clip,text_clip.set_position((0.18,.19),relative=True)])
            return cvc.set_duration(clip.duration)
        video = editor.VideoFileClip('./Video/crackers.mp4')
        w_text = self.parent.ids.first_screen.ids.wish_input.text
        n_text = self.parent.ids.first_screen.ids.name_input.text
        if w_text == '':
            w_text ='.'
        if n_text == '':
            n_text='.'
        subs = [((0,11),'.','black',10),
                ((11,16),(w_text + '\n\n'+ n_text),'yellow',80),
                ((16,17),'.','black',10,)]
        annotated_clip= [annotate(video.subclip(from_t,to_t),txt,txt_color,fontsize) for (from_t,to_t),txt,txt_color,fontsize in subs]
        final = editor.concatenate_videoclips(annotated_clip)
        vid_name = random.randint(100000,999999)
        final.write_videofile(str(vid_name) + '.mp4',fps=24,codec='mpeg4')
       
    def start_vid(self,*args):
        self.download= Thread(target = self.movie)
        self.download.start()
    def progress_screen(self,*args):
        if self.ids.download_btn.state == 'down':
            self.ids.count.opacity = 1
            self.ids.progress.opacity = 1
            self.ids.cancel.opacity = 1
            self.ids.cancel.disabled = False
            self.ids.download_btn.opacity = 0
            self.ids.download_btn.disabled = True
    def del_progress_screen(self,*args):
        self.ids.count.opacity = 0
        self.ids.progress.opacity = 0
        self.ids.cancel.opacity = 0
        self.ids.cancel.disabled = True
        self.ids.download_btn.opacity = 1
        self.ids.download_btn.disabled = False
    def close_dialog(self,*args):
        self.dialog_box.dismiss()
        self.del_progress_screen()
        self.parent.current = 'first_screen'
    
        
        
        
        
        
        
    
