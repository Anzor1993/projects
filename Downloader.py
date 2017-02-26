from tkinter import *
from tkinter import ttk
from pytube import YouTube
from pprint import pprint
import re


class Downloader(YouTube):
    def __init__(self):
        self.root = Tk()
        self.root['bg'] = '#EFEBDC'
        self.format_choice = IntVar()
        self.root.title('Youtube Downloader')
        self.root.geometry('494x500')
        self.frame1 = Frame(self.root, bg = '#888175', bd = 5)
        self.lbl = Label(self.root, text = 'Вставьте ссылку в поле', bg = '#888175', fg = 'white', bd = 5)
        self.pwent = Text(self.root, height = 2, width = 60)
        self.paramms = Text(self.frame1, height = 10, width = 60)
        self.lbl2 = Label(self.frame1, text = 'Введите нужную вам директорию,\nнапример "D:/"', bg ='#888175', fg = 'white')
        self.correct_dir = Entry(self.frame1,width = 10)
        self.btn1 = Button(self.frame1, text= 'Скачать', bg = '#B9B9A8', command = self.loadd)
        self.btn2 = Button(self.frame1, text= 'Посмотреть параметры видео', bg= '#B9B9A8', command= self.param)
        self.format_choice = StringVar()
        self.format_choice.set(None)
        self.frame1.grid(row = 5, column = 2)
        self.lbl.grid(row =0, column = 1, columnspan= 3)
        self.pwent.grid(row = 4, column = 2, columnspan = 4)
        self.paramms.grid(row = 6, column = 2, columnspan = 4)
        self.btn1.grid(row = 5, column = 2)
        self.btn2.grid(row = 5, column = 4)
        self.lbl2.grid(row = 7, column = 2)
        self.correct_dir.grid(row = 7, column = 4)
        self.root.mainloop()
    def get_formats(self):
        self.lbl2 = Label(self.root, text = "Выберите необходимый формат видео\n и нажмите кнопку 'скачать'", bg = 'green', fg = 'white', bd = 5)
        self.lbl2.grid(row = 11, column = 2)
        self.rb1 = Radiobutton(self.root, text = 'mp4 + 720p', variable=self.format_choice, bg = '#EFEBDC', value = 1, command = self.update)
        self.rb2 = Radiobutton(self.root, text = 'mp4 + 360p', variable=self.format_choice, bg = '#EFEBDC', value = 2, command = self.update)
        self.rb3 = Radiobutton(self.root, text = '3gp + 240p', variable=self.format_choice, bg = '#EFEBDC', value = 3, command = self.update)
        self.rb4 = Radiobutton(self.root, text = '3gp + 144p', variable=self.format_choice, bg = '#EFEBDC', value = 4, command = self.update)
        self.rb1.grid(row = 7, column = 2)
        self.rb2.grid(row = 8, column = 2)
        self.rb3.grid(row = 9, column = 2)
        self.rb4.grid(row = 10, column = 2)
    def loadd(self):
        self.dir = self.correct_dir.get()
        self.get_formats()
        self.param()
        self.format1 = 'mp4'
        self.format2 = '3gp'
        self.format3 = '720p'
        self.format4 = '360p'
        self.format5 = '240p'
        self.format6 = '144p'
        self.except_error = 'К сожалению, видео не поддерживает выбранный вами формат.\nВыберите, пожалуйста, любой формат из перечисленных ниже:\n\n' + '\n'.join(map(str, self.yt.get_videos()))
        self.ssilka = self.pwent.get('1.0', END)
        self.yt = YouTube(self.ssilka)
        if int(self.format_choice.get()) == 1:
            try:
                self.video = self.yt.get(self.format1, self.format3)
                self.video.download(self.dir)#D:/
            except:
                self.paramms.delete(0.0, END)
                self.paramms.insert(0.0, self.except_error)        
        elif int(self.format_choice.get()) == 2:
            try:
                self.video = self.yt.get(self.format1, self.format4)
                self.video.download(self.dir)
            except:
                self.paramms.delete(0.0, END)
                self.paramms.insert(0.0, self.except_error)
        elif int(self.format_choice.get()) == 3:
            try:
                self.video = self.yt.get(self.format2, self.format5)
                self.video.download(self.dir)
            except:
                self.paramms.delete(0.0, END)
                self.paramms.insert(0.0, self.except_error)
        elif int(self.format_choice.get()) == 4:
            try:
                self.video = self.yt.get(self.format2, self.format6)
                self.video.download(self.dir)
            except:
                self.paramms.delete(0.0, END)
                self.paramms.insert(0.0, self.except_error)
    def param(self):
        self.get_formats()
        self.ssilka = self.pwent.get('1.0', END)
        self.yt = YouTube(self.ssilka)
        self.formats_video = 'Доступные форматы видео: \n\n' + '\n'.join(map(str, self.yt.get_videos())) + '\n\nНазвание видео: ' + self.yt.filename
        self.paramms.delete(0.0, END)
        self.paramms.insert(0.0, self.formats_video)
    def update(self):
        return self.format_choice.get()

start = Downloader()
input('нажмите Enter, чтобы выйти')


