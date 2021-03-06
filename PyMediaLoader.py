from __future__ import unicode_literals
import youtube_dl
import os
import traceback
import sys
from kivy.core.window import Window
from kivy.app import App
from kivy.graphics.instructions import Canvas
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class Karkas(Widget):
    def __init__(self):
        super(Karkas, self).__init__()
        Window.size = (500, 200)
        Window.clearcolor = (0, 1, 0, 1)
        self.add_widget(Label(text = 'Audio (mp3)', pos=(30, 135), color = (0,0,1,1)))
        self.add_widget(Label(text = 'Video (mp4)', pos=(30, 105), color = (0,0,1,1)))
        self.add_widget(Label(text = 'Вставьте ссылку в поле ввода', pos = (200, 0), color = (0,0,1,1)))
        self.url_input = TextInput(multiline=False, width = 500, height = 30, pos = (0, 70))
        self.add_widget(self.url_input)
        self.button_run = Button(pos =(200, 100), width = 80, height = 80, font_size = 15, background_normal = 'dow1.png', background_down = 'dow2.png')
        self.button_run.bind(on_press = self.go_go)
        self.add_widget(self.button_run)
        self.btn1 = ToggleButton(text = '1', color = (0,0,0,0), group = 'formats', pos=(15, 180), width = 10, height = 10)
        self.btn1.bind(on_press = self.change_value1)
        self.btn2 = ToggleButton(text = '2', color = (0,0,0,0), group = 'formats', pos=(15, 150), width = 10, height = 10)
        self.btn2.bind(on_press = self.change_value2)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.value = 0
    def change_value2(self,btn2):
        if self.btn2.state == 'down':
            self.value = 2
    def change_value1(self,btn1):
        if self.btn1.state == 'down':
            self.value = 1
    def go_go(self, button_run):
        if self.value == 1:
            self.audio_load()
        elif self.value == 2:
            self.video_load()
        else:
            print('Сначала выберите формат файла: аудио или видео')
            
class Loader(Karkas):
    
    def __init__(self):
        super().__init__()
        
    def audio_load(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.url_input.text])
    def video_load(self):
        self.ydl_opts = {
            'format':'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
        }
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([self.url_input.text])
class PyMediaLoader(App):
    def build(self):
        self.icon = 'Button-Download-icon.png'
        return Loader()
try:
    #Проверяем не установлена ли ffmpeg на компьютере, если нет, то скачиваем
    if os.path.exists('C:/ffmpeg') is False:
        os.startfile('cmd.exe', 'runas')
        print('Добро пожаловать!\n\
\t 1. Скопируйте на диск С папку ffmpeg\n\
\t 2. Введите в командной строке set | findstr "^Path"\n\
\t 3. Скопируйте появившуюся строку \n\
\t 4. Введите setx /M PATH "скопированная строка\;c:\ffmpeg\bin"\n\
\t 5. Нажмите Enter')
    else:
        print('Добро пожаловать! Чтобы скачать видео\n\
или аудио:\n\
\t 1. Вставьте ссылку в поле ввода\n\
\t 2. Выберите формат (аудио или видео)\n\
\t 3. Нажмите кнопку "скачать"\n\
\t 4. Файл должен скачаться в папку с exe файлом.')
        if __name__ == '__main__':
            PyMediaLoader().run()  
except Exception:
    print (''.join(traceback.format_exception(*sys.exc_info())))#выводит ошибку на экран
    input('enter')


