import subprocess
import psutil
import os
import random
from tkinter import *


def f(x):
    cmd = None
    local_name = random.randrange(1, 100)
    if int(choice_format()) == 1:
        cmd = 'ffmpeg -f dshow  -i video="screen-capture-recorder"  -r 20 -t 1500 %d.flv' % local_name
    elif int(choice_format()) == 2:
        cmd = 'ffmpeg -f dshow -i video="screen-capture-recorder" -r 20 -t 1500 %d.avi' % local_name
    global proc
    #если х = 1 то запускаем ffmpeg 
    if x == 1 and cmd != None :
        info_table.delete(0.0, END)
        info_table.insert(0.0, 'идёт запись...')
        proc = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE) # stderr = subprocess.STDOUT)
    elif x == 2 and cmd != None:
        info_table.delete(0.0, END)
        info_table.insert(0.0, 'видео сохранено в\nпапку с exe файлом!')
        #полное завершение процесса с помощью модуля psutil 
        parent = psutil.Process(proc.pid)
        for child in parent.children(recursive=True):  
            child.kill()
        parent.kill()
    else:
        info_table.delete(0.0, END)
        info_table.insert(0.0, 'сначала выберите\nформат конечного\nфайла...')        
def rec():
    f(1)
def stop():
    f(2)
def choice_format():
    return format_choice.get()

    
    
'''СОЗДАЕМ ГРАФИЧЕСКИЙ ИНТЕРФЕЙС'''
root = Tk()
root.geometry('270x250')
root.title('.')
root['bg'] = '#d87c55'
root.iconbitmap('icon.ico')#иконка приложения
format_choice = IntVar()
#создаем рамки
frame = Frame(root)
frame.grid(row = 2, column = 2)
frame2 = Frame(root, bg = '#d87c55')
frame2.grid(row = 4, column = 2)
label = Label(frame2, text = 'сначала выберите формат конечного файла', bg = '#d87c55', fg = 'black')
label.grid(row = 3, column = 1)
#создаем переключатели
format1 = Radiobutton(frame2, text = 'flv', variable = format_choice, value = 1, bg = '#d87c55', fg = 'black',  command = choice_format)
format1.grid(row = 4, column = 1)
format2 = Radiobutton(frame2, text = 'avi', variable = format_choice, value = 2, bg = '#d87c55', fg = 'black', command = choice_format)
format2.grid(row = 5, column = 1)
#информационное табло
info_table = Text(frame2, height = 5, width = 20)
info_table.grid(row = 2, column = 1)
#кнопки и иконки для них
icon1 = PhotoImage(file = 'rec.png')
icon2 = PhotoImage(file = 'stop.png')
btn1 = Button(frame, compound = TOP, text='запись', width = 35, height = 40, bg = '#e74545', fg = 'white', image = icon1, command = rec)
btn1.grid(row = 1, column = 1)
btn2 = Button(frame, compound = TOP, text='стоп', width = 35, height = 40, bg = '#e74545', fg = 'white', image = icon2, command = stop)
btn2.grid(row = 1, column = 3)

   
root.mainloop()
        


