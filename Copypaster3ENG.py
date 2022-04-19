###############|the first line|###############

#Copypaster v3.2 by echo complex

#open source code

#https://github.com/echocomplex

#https://t.me/echoscode

############################################################################

#connecting libraries

import pyautogui
import time
import colorama
from colorama import Fore, init
from tkinter import *  
init()  

#creating a window and editing it

window = Tk() 
window['bg'] = '#5a5a5a'
window.title("Copypaster 3")  
window.geometry('430x494')  
window.resizable(width=False, height=False)
window.iconbitmap('icon.ico')

#distribution of variables

messages = IntVar()
time1 = DoubleVar()
message1 = StringVar()
message2 = StringVar()
message3 = StringVar()
message4 = StringVar()

#connecting and using variables

def clicked():
    print(Fore.LIGHTGREEN_EX + '          DEBUG CONSOLE')
    print(Fore.GREEN + ' -------------------------------')
    print(Fore.GREEN + ' -------------------------------')
    print(Fore.GREEN + ' -------------------------------')
    print(' ')
    if messages.get() == 0:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            a = a + 1
            print(Fore.CYAN + str(a), 'cycle is completed.')
    elif messages.get() == 1:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message1.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            a = a + 1
            print(Fore.CYAN + ' ' + str(a), 'cycle is completed.')
    elif messages.get() == 2:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message1.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message2.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            a = a + 1
            print(Fore.CYAN + ' ' + str(a), 'cycle is completed.')
    elif messages.get() == 3:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message1.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message2.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message3.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            a = a + 1
            print(Fore.CYAN + ' ' +  str(a), 'cycle is completed.')
    elif messages.get() == 4:
        a = 0
        while True:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message1.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message2.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message3.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            pyautogui.typewrite(message4.get())
            pyautogui.press('Enter')
            time.sleep(float(time1.get()))
            a = a + 1
            print(Fore.CYAN + ' ' +  str(a), 'cycle is completed.')
    else:
        print(Fore.RED + ' ' +  "!!! Critical error! An incorrect value was entered. The program will restart in 5 seconds !!!")
        time.sleep(5)
        quit()

#widgets 

lbl = Label(window, text="Copypaster v3.2 by echo complex", font=("Arial Bold", 20), fg='#8b00ff')  
lbl.pack(side=TOP)

lbl2 = Label(window, text="Number of additional messages (0-4)", font=1)
lbl2.place(x=80, y=40)

txt = Entry(textvariable=messages, width=10)   
txt.place(x=180, y=70)

lbl3 = Label(window, text="Delay between messages (In seconds)", font=1)
lbl3.place(x=75, y=100)

txt2 = Entry(textvariable=time1, width=10)     
txt2.place(x=180, y=130)

lbl8 = Label(window, text="Additional messages support only ENG", font=1, fg='BLUE')
lbl8.place(x=73, y=155)

lbl4 = Label(window, text="First message", font=1)
lbl4.place(x=160, y=190)

txt3 = Entry(textvariable=message1, width=30)     
txt3.place(x=120, y=220)

lbl5 = Label(window, text="Second message", font=1)
lbl5.place(x=148, y=250)

txt4 = Entry(textvariable=message2, width=30)     
txt4.place(x=120, y=280)

lbl6 = Label(window, text="Third message", font=1)
lbl6.place(x=158, y=310)

txt5 = Entry(textvariable=message3, width=30)     
txt5.place(x=120, y=340)

lbl7 = Label(window, text="Fourth message", font=1)
lbl7.place(x=152, y=370)

txt6 = Entry(textvariable=message4, width=30)     
txt6.place(x=120, y=400)

lbl7 = Label(window, text="!!! Works if ENG layout is enabled !!!", font=1, fg='RED')
lbl7.place(x=83, y=430)

btn = Button(window, text="Start", width=15, command=clicked)  
btn.pack(side=BOTTOM)

#looping window

window.mainloop()


###############|the last line|###############
