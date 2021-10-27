#!/usr/bin/env python
# coding: utf-8
# By KK;2021.10.25;kyle.liu@mazars.cn
import tkinter as tk
import os
from tkinter.filedialog import askdirectory
window = tk.Tk()
 

window.title('EZGE')
 

window.geometry('500x600') 
canvas = tk.Canvas(window, height=100, width=400)
image_file = tk.PhotoImage(file='./Mazars_l.gif')
image = canvas.create_image(170, 10, anchor='n',image=image_file)
#canvas.pack(side='bottom')
canvas.place(x=0,y=520)

tk.Label(window, text='Name:', font=('Arial', 14)).place(x=10, y=90)
tk.Label(window, text='Position:', font=('Arial', 14)).place(x=10, y=130)
tk.Label(window, text='Device:', font=('Arial', 14)).place(x=10, y=170)
tk.Label(window, text='Model:', font=('Arial', 14)).place(x=10, y=210)
tk.Label(window, text='S/N:', font=('Arial', 14)).place(x=10, y=250)
tk.Label(window, text='Assest Number:', font=('Arial', 14)).place(x=10, y=290)
tk.Label(window, text='Media Type:', font=('Arial', 14)).place(x=10, y=330)
tk.Label(window, text='Model(HD):', font=('Arial', 14)).place(x=10, y=370)
tk.Label(window, text='SN:', font=('Arial', 14)).place(x=10, y=410)
 

v1 = tk.StringVar()
e1 = tk.Entry(window, textvariable=v1, font=('Arial', 14))
e1.place(x=160,y=90)
#
v2 = tk.StringVar()
e2 = tk.Entry(window, textvariable=v2, font=('Arial', 14))
e2.place(x=160,y=130)
#
v3 = tk.StringVar()
e3 = tk.Entry(window, textvariable=v3, font=('Arial', 14))
e3.place(x=160,y=170)
#
v4 = tk.StringVar()
e4 = tk.Entry(window, textvariable=v4, font=('Arial', 14))
e4.place(x=160,y=210)
# 
v5 = tk.StringVar()
e5 = tk.Entry(window, textvariable=v5, font=('Arial', 14))
e5.place(x=160,y=250)
# 
v6 = tk.StringVar()
e6 = tk.Entry(window, textvariable=v6, font=('Arial', 14))
e6.place(x=160,y=290)
#
v7 = tk.StringVar()
e7 = tk.Entry(window, textvariable=v7, font=('Arial', 14))
e7.place(x=160,y=330)
#
v8 = tk.StringVar()
e8 = tk.Entry(window, textvariable=v8, font=('Arial', 14))
e8.place(x=160,y=370)
#
v9 = tk.StringVar()
e9 = tk.Entry(window, textvariable=v9, font=('Arial', 14))
e9.place(x=160,y=410)
    
def print_note():
    Name = v1.get()
    Position = v2.get()
    Manufacturer = v3.get()
    M_pc = v4.get()
    SN = v5.get()
    Assest_Number = v6.get()
    Manufacturer_storage = v7.get()
    Model = v8.get()
    Interface = v9.get()

    if Name == '':
        Name = ''
    else:
        print('Name:'+Name)
        print('')
        Name = Name+', '

    if Position == '':
        Position = ''
    else:
        print('Position:'+Position)
        print('')
        Position = 'Position:'+Position

    if Manufacturer == '':
        Manufacturer = ''
    else:
        print('Manufacturer:'+Manufacturer)
        print('')
        Manufacturer = 'Device:'+Manufacturer+' '+M_pc+', '

    if SN == '':
        SN = ''
    else:
        print('S/N:'+SN)
        print('')
        SN = 'S/N:'+SN+', '
        
    if Assest_Number == '':
        Assest_Number = ''
    else:
        print('Assest Number:'+Assest_Number)
        print('')
        Assest_Number = 'Assest Number:'+Assest_Number

    if Manufacturer_storage == '':
        Manufacturer_storage = ''
    else:
        print('Manufacturer_storage:'+Manufacturer_storage)
        print('')
        Manufacturer_storage = 'Media Type:'+Manufacturer_storage+' '+Model+', '

    #if Storage == '':
    #    Storage = 'N/A'
    #else:
    #    print('Storage:'+Storage)
    #    print('')
    #    Storage ='Storage:'+Storage+' '

    if Interface == '':
        Interface = ''
    else:
        print('Interface:'+Interface)
        print('')
        Interface = 'SN:'+Interface
    
    folder_name = v10.get()
    c = path.get()
    with open(''+c+'/'+folder_name+'/03_Notes/Notes.txt','w') as f:
        f.write(Name+Position+"; "+Manufacturer+SN+Assest_Number+"; "+Manufacturer_storage+Interface)

b1 = tk.Button(window, text='Generate Notes', width=15, height=2, font=('Times New Roman', 16),command=print_note)
b1.place(x=140,y=430)

def create_folders():
    folder_name = v10.get()
    c = path.get()
    os.makedirs(''+c+'/'+folder_name+'/01_Forensic Image_E01')
    os.makedirs(''+c+'/'+folder_name+'/02_Photos')
    os.makedirs(''+c+'/'+folder_name+'/03_Notes')
def get_path():
        dirpath = askdirectory()
        path.set(dirpath)
#
v10 = tk.StringVar()
v10.set('S9990101A')
e10 = tk.Entry(window, textvariable=v10, font=('Arial', 14))
e10.place(x=50,y=50)

b2 = tk.Button(window, text='Generate Folders', width=15, height=1, font=('Times New Roman', 14),command=create_folders)
b2.place(x=300,y=50)
#
path = tk.StringVar()
e11 = tk.Entry(window, textvariable=path,font=('Arial', 14))
e11.place(x=50,y=10)
b3 = tk.Button(window, text='Choose Path', width=15, height=1, font=('Times New Roman', 14),command=get_path)
b3.place(x=300,y=10)

window.mainloop()
