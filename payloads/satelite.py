from  mss import mss
import os
import sys

screen = mss()


def collectimage():
    try:
        if sys.platform == "win32":
            dest_path =  os.path.expandvars("%userprofile%") +'\\Documents\\'
        else:
            dest_path = os.path.expanduser('~')
        
        screen.shot(mon=-1, output=(dest_path + 'tempic.png'))
        
        return True

    except:
        return False    

            
    